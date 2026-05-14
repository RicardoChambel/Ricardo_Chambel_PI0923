/* ── Power Chord — script.js (API integration) ── */

// ── Config ─────────────────────────────────────────────
const API_URL = "http://localhost:5163/api";

// ── State ──────────────────────────────────────────────
let currentUser = null;   // { email, token }
let concertsData = [];

// ── Init ───────────────────────────────────────────────
document.addEventListener('DOMContentLoaded', () => {
    // Restore session from localStorage (token + email)
    const saved = localStorage.getItem('pc_session');
    if (saved) {
        try {
            currentUser = JSON.parse(saved);
            updateUI();
        } catch { localStorage.removeItem('pc_session'); }
    }

    // Password strength meter
    const pwInput = document.getElementById('registerPassword');
    if (pwInput) pwInput.addEventListener('input', () => updateStrength(pwInput.value));

    // Price preview on change
    const qtyInput = document.getElementById('quantity');
    const idInput  = document.getElementById('concertId');
    if (qtyInput) qtyInput.addEventListener('input', updatePricePreview);
    if (idInput)  idInput.addEventListener('input', updatePricePreview);

    // Load concerts on boot
    loadConcerts();
});

// ── Tab switching ──────────────────────────────────────
function switchTab(tab) {
    document.getElementById('tabRegister').classList.toggle('tab-content--hidden', tab !== 'register');
    document.getElementById('tabLogin').classList.toggle('tab-content--hidden', tab !== 'login');
    document.querySelectorAll('.tab').forEach((el, i) => {
        el.classList.toggle('tab--active', (i === 0 && tab === 'register') || (i === 1 && tab === 'login'));
    });
}

// ── Auth ───────────────────────────────────────────────
async function register() {
    const email        = val('registerEmail');
    const passwordHash = val('registerPassword');

    if (!email || !passwordHash) return showMsg('Preenche todos os campos.', 'error');
    if (!validEmail(email))      return showMsg('Email inválido.', 'error');
    if (passwordHash.length < 6) return showMsg('A password precisa de pelo menos 6 caracteres.', 'error');

    try {
        const res = await fetch(`${API_URL}/Auth/register`, {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ email, passwordHash })
        });

        const text = await res.text();

        if (!res.ok || text.toLowerCase().includes('já está registado')) {
            showMsg(text || 'Erro ao registar.', 'error');
            return;
        }

        showMsg('Conta criada com sucesso!', 'success');
        switchTab('login');
        document.getElementById('loginEmail').value = email;

    } catch {
        showMsg('Erro de ligação ao servidor.', 'error');
    }
}

async function login() {
    const email        = val('loginEmail');
    const passwordHash = val('loginPassword');

    if (!email || !passwordHash) return showMsg('Preenche todos os campos.', 'error');

    try {
        const res = await fetch(`${API_URL}/Auth/login`, {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ email, passwordHash })
        });

        if (!res.ok) return showMsg('Credenciais inválidas.', 'error');

        const data = await res.json();

        currentUser = { email, token: data.token };
        localStorage.setItem('pc_session', JSON.stringify(currentUser));

        updateUI();
        showMsg('Bem-vindo de volta!', 'success');

    } catch {
        showMsg('Erro de ligação ao servidor.', 'error');
    }
}

function logout() {
    currentUser = null;
    localStorage.removeItem('pc_session');
    updateUI();
    showMsg('Sessão terminada.', 'info');
}

function updateUI() {
    const logged = !!currentUser;
    document.getElementById('authSection').style.display = logged ? 'none' : 'block';
    document.getElementById('userSection').style.display = logged ? 'block' : 'none';
    document.getElementById('headerStatus').textContent  = logged ? `● ${currentUser.email}` : '';

    if (logged) {
        document.getElementById('userAvatar').textContent = currentUser.email[0].toUpperCase();
        document.getElementById('userName').textContent   = currentUser.email;
        renderMyTickets();
    } else {
        document.getElementById('myTickets').innerHTML = '<p class="empty-state">Sem bilhetes ainda.</p>';
    }
}

// ── Concerts ───────────────────────────────────────────
async function loadConcerts() {
    const grid = document.getElementById('concerts');
    const btn  = document.getElementById('loadBtn');

    // Skeleton
    grid.innerHTML = [1,2,3].map(() => `<div class="skeleton"></div>`).join('');
    if (btn) {
        btn.disabled = true;
        btn.querySelector('svg').style.animation = 'spin 0.8s linear infinite';
    }

    // Add spin keyframe once
    if (!document.getElementById('spinStyle')) {
        const s = document.createElement('style');
        s.id = 'spinStyle';
        s.textContent = '@keyframes spin { to { transform: rotate(360deg); } }';
        document.head.appendChild(s);
    }

    try {
        const res = await fetch(`${API_URL}/Concert`);
        if (!res.ok) throw new Error('API error');
        const raw = await res.json();

        // Normalise field names: API may return camelCase (name, date, location, price, id)
        concertsData = raw.map(c => ({
            id:       c.id,
            artist:   c.name  || c.artist  || '—',
            venue:    c.location || c.venue || '—',
            date:     c.date,
            price:    c.price,
            capacity: c.capacity ?? 100,
            sold:     c.sold     ?? 0
        }));

    } catch {}

    renderConcerts();
    if (btn) { btn.disabled = false; btn.querySelector('svg').style.animation = ''; }
}

function renderConcerts() {
    const grid = document.getElementById('concerts');
    if (!concertsData.length) {
        grid.innerHTML = '<p class="empty-state">Nenhum concerto disponível.</p>';
        return;
    }

    grid.innerHTML = concertsData.map(c => {
        const avail   = c.capacity - c.sold;
        const pct     = Math.min(100, Math.round((c.sold / c.capacity) * 100));
        const lvl     = pct > 80 ? 'avail--low' : 'avail--ok';
        const dateStr = formatDate(c.date);
        const availText = avail <= 0 ? 'Esgotado' : `${avail} lugares`;

        return `
        <div class="concert-card" onclick="selectConcert(${c.id})" id="concert-${c.id}">
            <div>
                <p class="concert-id-badge">ID #${c.id}</p>
                <p class="concert-artist">${esc(c.artist)}</p>
                <div class="concert-meta">
                    <span class="concert-tag">
                        <svg viewBox="0 0 12 12" fill="none"><rect x="1" y="2" width="10" height="9" rx="1" stroke="currentColor" stroke-width="1.1"/><path d="M1 5h10M4 1v2M8 1v2" stroke="currentColor" stroke-width="1.1" stroke-linecap="round"/></svg>
                        ${dateStr}
                    </span>
                    <span class="concert-tag">
                        <svg viewBox="0 0 12 12" fill="none"><path d="M6 1C4.3 1 3 2.3 3 4c0 2.5 3 7 3 7s3-4.5 3-7c0-1.7-1.3-3-3-3Z" stroke="currentColor" stroke-width="1.1"/><circle cx="6" cy="4" r="1" fill="currentColor"/></svg>
                        ${esc(c.venue)}
                    </span>
                    <span class="concert-tag">${availText}</span>
                </div>
                <div class="avail-bar">
                    <div class="avail-bar-fill ${lvl}" style="width:${pct}%"></div>
                </div>
            </div>
            <div class="concert-price-badge">
                <p class="price-num">${c.price}€</p>
                <p class="price-unit">p/bilhete</p>
            </div>
        </div>`;
    }).join('');
}

function selectConcert(id) {
    document.querySelectorAll('.concert-card').forEach(el => el.classList.remove('selected'));
    const card = document.getElementById(`concert-${id}`);
    if (card) card.classList.add('selected');
    document.getElementById('concertId').value = id;
    updatePricePreview();
    document.querySelector('.panel--buy')?.scrollIntoView({ behavior: 'smooth', block: 'start' });
}

function updatePricePreview() {
    const id      = parseInt(val('concertId'));
    const qty     = parseInt(val('quantity')) || 1;
    const concert = concertsData.find(c => c.id === id);
    const preview = document.getElementById('pricePreview');
    const priceEl = document.getElementById('priceValue');

    if (concert && qty > 0) {
        preview.style.display = 'flex';
        priceEl.textContent = `${(concert.price * qty).toFixed(2)}€`;
    } else {
        preview.style.display = 'none';
    }
}

// ── Buy ────────────────────────────────────────────────
async function buyTicket() {
    if (!currentUser){
        switchTab('login');
        return showMsg('Faz login para comprar bilhetes.', 'error');
    } 

    const concertId = parseInt(val('concertId'));
    const quantity  = parseInt(val('quantity'));

    if (!concertId || isNaN(concertId)) return showMsg('Introduz um ID de concerto válido.', 'error');
    if (!quantity  || quantity < 1)     return showMsg('Quantidade inválida.', 'error');
    if (quantity > 10)                  return showMsg('Máximo de 10 bilhetes por compra.', 'error');

    const concert = concertsData.find(c => c.id === concertId);
    if (!concert) return showMsg(`Concerto #${concertId} não encontrado.`, 'error');

    const avail = concert.capacity - concert.sold;
    if (avail < quantity) return showMsg(`Apenas ${avail} bilhetes disponíveis.`, 'error');

    try {
        const res = await fetch(`${API_URL}/Ticket`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'Authorization': `Bearer ${currentUser.token}`
            },
            body: JSON.stringify({ concertId, quantity })
        });

        if (!res.ok) {
            const err = await res.text();
            showMsg('Erro ao comprar bilhete: ' + (err || res.status), 'error');
            return;
        }

        // Optimistic local update so the bar reflects instantly
        concert.sold += quantity;

        renderConcerts();
        updatePricePreview();
        renderMyTickets();

        showMsg(`${quantity} bilhete(s) para ${concert.artist} comprado(s)!`, 'success');

        document.getElementById('concertId').value = '';
        document.getElementById('quantity').value  = '1';
        document.getElementById('pricePreview').style.display = 'none';
        document.querySelectorAll('.concert-card').forEach(el => el.classList.remove('selected'));

    } catch {
        showMsg('Erro de ligação ao servidor.', 'error');
    }
}

// ── My Tickets ─────────────────────────────────────────
// Fetches the user's tickets from the API if a /Ticket/my endpoint exists,
// otherwise keeps the local optimistic list built during the session.
let sessionTickets = [];   // accumulates purchases made in this session

async function renderMyTickets() {
    const container = document.getElementById('myTickets');
    if (!currentUser) return;

    // Try to fetch from API
    try {
        const res = await fetch(`${API_URL}/Ticket`, {
            headers: { 'Authorization': `Bearer ${currentUser.token}` }
        });

        if (res.ok) {
            const list = await res.json();
            if (!list.length) {
                container.innerHTML = '<p class="empty-state">Sem bilhetes ainda</p>';
                return;
            }
            container.innerHTML = list.slice().reverse().map(t => {
                const artist = t.concertName || t.artist || `Concerto #${t.concertId}`;
                const date   = t.date ? formatDate(t.date) : '';
                const total  = t.totalPrice ?? (t.price * t.quantity) ?? '—';
                return `
                <div class="ticket-item">
                    <strong>${esc(artist)}</strong>
                    <span>${date ? date + ' · ' : ''}${t.quantity}× · ${typeof total === 'number' ? total.toFixed(2) + '€' : total}</span>
                </div>`;
            }).join('');
            return;
        }
    } catch { /* API doesn't expose this endpoint — fall through */ }

    // Fallback: show tickets bought in the current session
    if (!sessionTickets.length) {
        container.innerHTML = '<p class="empty-state">Sem bilhetes ainda</p>';
        return;
    }
    container.innerHTML = sessionTickets.slice().reverse().map(t => `
        <div class="ticket-item">
            <strong>${esc(t.artist)}</strong>
            <span>${formatDate(t.date)} · ${t.qty}× · ${(t.price * t.qty).toFixed(2)}€</span>
        </div>
    `).join('');
}

// Track session purchases for the fallback
const _origBuy = buyTicket;
// Patch: after a successful buy, push to sessionTickets before renderMyTickets is called.
// We wrap buyTicket post-hoc so the original flow is unchanged.
(function patchBuyForSession() {
    const origBuy = window.buyTicket;
    window.buyTicket = async function () {
        const concertId = parseInt(val('concertId'));
        const quantity  = parseInt(val('quantity'));
        const concert   = concertsData.find(c => c.id === concertId);
        const before    = document.querySelectorAll('.ticket-item').length;

        await origBuy();

        // If a new ticket-item appeared, also push to sessionTickets
        const after = document.querySelectorAll('.ticket-item').length;
        if (concert && after > before) {
            sessionTickets.push({ artist: concert.artist, date: concert.date, qty: quantity, price: concert.price });
        }
    };
})();

// ── Quantity helpers ───────────────────────────────────
function adjustQty(delta) {
    const input = document.getElementById('quantity');
    const v = Math.min(10, Math.max(1, (parseInt(input.value) || 1) + delta));
    input.value = v;
    updatePricePreview();
}

// ── Password strength ──────────────────────────────────
function updateStrength(pw) {
    const bar = document.getElementById('strengthBar');
    if (!bar) return;
    let score = 0;
    if (pw.length >= 6)           score++;
    if (pw.length >= 10)          score++;
    if (/[A-Z]/.test(pw))         score++;
    if (/[0-9]/.test(pw))         score++;
    if (/[^a-zA-Z0-9]/.test(pw)) score++;

    const pct   = Math.round((score / 5) * 100);
    const color = score < 2 ? '#e74c3c' : score < 4 ? '#f39c12' : '#27ae60';
    bar.style.setProperty('--strength', pct + '%');
    bar.style.setProperty('--strength-color', color);
}

// ── Toasts ─────────────────────────────────────────────
const icons = {
    success: `<svg class="message-icon" viewBox="0 0 16 16" fill="none"><path d="M2 8l4 4 8-8" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/></svg>`,
    error:   `<svg class="message-icon" viewBox="0 0 16 16" fill="none"><path d="M4 4l8 8M12 4l-8 8" stroke="currentColor" stroke-width="1.5" stroke-linecap="round"/></svg>`,
    info:    `<svg class="message-icon" viewBox="0 0 16 16" fill="none"><circle cx="8" cy="8" r="6" stroke="currentColor" stroke-width="1.2"/><path d="M8 7v4M8 5.5v.5" stroke="currentColor" stroke-width="1.2" stroke-linecap="round"/></svg>`,
};

function showMsg(text, type = 'info') {
    const div = document.getElementById('messageDiv');
    const msg = document.createElement('div');
    msg.className = `message ${type}`;
    msg.innerHTML = `${icons[type] || ''}<span>${text}</span>`;
    div.appendChild(msg);

    requestAnimationFrame(() => requestAnimationFrame(() => msg.classList.add('show')));

    setTimeout(() => {
        msg.classList.remove('show');
        msg.addEventListener('transitionend', () => msg.remove(), { once: true });
    }, 3500);
}

// ── Utilities ──────────────────────────────────────────
function val(id) {
    return (document.getElementById(id)?.value || '').trim();
}

function esc(str) {
    return String(str).replace(/[&<>"']/g, m =>
        ({ '&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;' })[m]
    );
}

function validEmail(e) {
    return /^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(e);
}

function formatDate(dateStr) {
    try {
        return new Date(dateStr).toLocaleDateString('pt-PT', { day: '2-digit', month: 'short', year: 'numeric' });
    } catch { return dateStr; }
}