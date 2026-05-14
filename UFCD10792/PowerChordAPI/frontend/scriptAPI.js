const API_URL = "http://localhost:5163/api";
let token = "";

function showMessage(text, type = "success") {
    const container = document.getElementById("messageDiv");

    const message = document.createElement("div");
    message.className = `message ${type}`;
    message.innerText = text;

    container.appendChild(message);

    setTimeout(() => {
        message.classList.add("show");
    }, 10);

    // desaparecer
    setTimeout(() => {
        message.classList.remove("show");

        setTimeout(() => {
            message.remove();
        }, 400);
    }, 1500);
}
async function register() {
    const email = document.getElementById("registerEmail").value;
    const passwordHash = document.getElementById("registerPassword").value;

    const response = await fetch(`${API_URL}/Auth/register`, {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({
            email,
            passwordHash
        })
    });

    const result = await response.text();
    if(result == "Este email já está registado."){
        showMessage(result, "error");
    }else{
        showMessage(result, "success");
        
        window.location.reload();
    }
}

async function login() {
    const email = document.getElementById("loginEmail").value;
    const passwordHash = document.getElementById("loginPassword").value;

    const response = await fetch(`${API_URL}/Auth/login`, {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({
            email,
            passwordHash
        })
    });

    if (!response.ok) {
        showMessage("Credenciais Inválidas!", "error");
        return;
    }

    const data = await response.json();
    token = data.token;

    showMessage("Login feito com sucesso", "success");
}

async function loadConcerts() {
    const btn = document.getElementById('verConcertosBtn');
    const response = await fetch(`${API_URL}/Concert`);
    const concerts = await response.json();

    const container = document.getElementById("concerts");
    container.innerHTML = "";

    concerts.forEach(concert => {
        container.innerHTML += `
            <div class="concert">
                <h3>${concert.name}</h3>
                <p><strong>ID:</strong> ${concert.id}</p>
                <p><strong>Local:</strong> ${concert.location}</p>
                <p><strong>Data:</strong> ${new Date(concert.date).toLocaleString()}</p>
                <p><strong>Preço:</strong> ${concert.price}€</p>
            </div>
        `;
    });
    btn.style.opacity = ".3";
}

async function buyTicket() {
    const concertId = Number(document.getElementById("concertId").value);
    const quantity = Number(document.getElementById("quantity").value);

    if (!token) {
        showMessage("Não está logado!", "error");
        return;
    }

    const response = await fetch(`${API_URL}/Ticket`, {
        method: "POST",
        headers: {
            "Content-Type": "application/json",
            "Authorization": `Bearer ${token}`
        },
        body: JSON.stringify({
            userId: "1",
            concertId,
            quantity
        })
    });

    if (!response.ok) {
        const error = await response.text();
        showMessage("Erro ao comprar bilhete: " + error, "error");
        return;
    }

    showMessage("Bilhete comprado com sucesso!", "success");
}