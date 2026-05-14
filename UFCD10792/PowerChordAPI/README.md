# PowerChordAPI

API REST em **ASP.NET Core 8** para gestão de concertos e venda de bilhetes da banda **Power Chord**.

Esta versão foi preparada para correr **sem Docker**, diretamente no Windows com Visual Studio ou terminal. O projeto mantém os componentes pedidos na tarefa: API REST, frontend, JWT, Swagger, base de dados, Redis, Polly, imposter Mountebank, scripts SQL, Postman e testes.

---

## Funcionalidades

- Registo e login de utilizadores
- Autenticação e autorização com JWT
- Passwords guardadas com hash PBKDF2
- CRUD de concertos
- Compra e consulta de bilhetes
- Integração com imposter Mountebank para simular pagamentos e inventário
- Cache híbrido nos endpoints de leitura:
  - 1.º nível: cache local em memória (`IMemoryCache`)
  - 2.º nível: Redis, quando estiver disponível
  - fallback: base de dados
- Resiliência com Polly:
  - retries automáticos
  - circuit breaker
- Documentação automática com Swagger/OpenAPI
- Frontend simples em HTML, CSS e JavaScript a consumir a API
- Scripts SQL de schema e seed
- Coleção Postman para testes manuais
- Testes automáticos básicos com xUnit

---

## Tecnologias utilizadas

- .NET 8
- ASP.NET Core Web API
- Entity Framework Core 8
- Entity Framework Core InMemory, para execução local simples
- SQL Server, opcional, através de connection string
- JWT Bearer Authentication
- Swagger / Swashbuckle
- Redis / StackExchange.Redis
- IMemoryCache
- Polly
- Mountebank
- xUnit
- HTML, CSS e JavaScript

---

## Estrutura do projeto

```text
PowerChordAPI/
├── PowerChordAPI/
│   ├── Controllers/
│   │   ├── AuthController.cs
│   │   ├── ConcertController.cs
│   │   ├── InventoryController.cs
│   │   └── TicketController.cs
│   ├── Data/
│   │   └── ApiContext.cs
│   ├── Models/
│   │   ├── Concert.cs
│   │   ├── Ticket.cs
│   │   └── User.cs
│   ├── Services/
│   │   └── PasswordService.cs
│   ├── Program.cs
│   ├── appsettings.json
│   └── PowerChordAPI.csproj
├── database/
│   ├── schema.sql
│   └── seed.sql
├── frontend/
│   ├── index.html
│   ├── script.js
│   ├── scriptAPI.js
│   └── style.css
├── imposter/
│   └── mountebank.json
├── postman/
│   └── PowerChordAPI.postman_collection.json
├── tests/
│   └── PowerChordAPI.Tests/
├── .env.example
├── start-api.bat
├── start-mountebank.bat
├── start-frontend.bat
└── README.md
```

---

## Requisitos para correr sem Docker

Obrigatório:

- **.NET SDK 8**
- **Node.js**, para correr o Mountebank com `npx`

Opcional:

- **Redis para Windows**, Memurai, Redis via WSL, ou outro servidor Redis local
- **SQL Server LocalDB / SQL Server Express**, caso não queira usar a base de dados em memória
- **Postman**, para importar a coleção de testes

> A API corre mesmo sem SQL Server configurado, porque usa `InMemoryDatabase` quando `ConnectionStrings:DefaultConnection` está vazio.

---

## Como executar sem Docker

### 1. Extrair o ZIP

Extraia o projeto para uma pasta, por exemplo:

```text
C:\Users\seu_utilizador\Desktop\Prog\PowerChordAPI_sem_Docker
```

---

### 2. Abrir um terminal na raiz do projeto

A pasta correta é a que contém o ficheiro `PowerChordAPI.sln`.

Exemplo:

```powershell
cd C:\Users\seu_utilizador\Desktop\Prog\PowerChordAPI_sem_Docker\PowerChordAPI
```

---

### 3. Correr o imposter Mountebank

Abra um terminal na raiz do projeto e execute:

```powershell
npx mb --configfile imposter\mountebank.json --allowInjection
```

Também pode usar o ficheiro:

```text
start-mountebank.bat
```

O Mountebank fica disponível em:

```text
http://localhost:2525
```

Os endpoints simulados ficam em:

```text
POST http://localhost:3000/payments
GET  http://localhost:3000/inventory/{sku}
```

---

### 4. Correr Redis, opcional

Se tiver Redis instalado localmente, inicie-o antes da API.

Exemplo:

```powershell
redis-server
```

A API está configurada para tentar usar:

```text
localhost:6379
```

Se o Redis não estiver disponível, a API continua a funcionar com cache local e base de dados. O Redis serve para cumprir a parte de cache distribuído e melhorar desempenho.

---

### 5. Correr a API

Na raiz do projeto, pode usar:

```text
start-api.bat
```

Ou manualmente:

```powershell
cd PowerChordAPI
dotnet restore
dotnet run --urls "http://localhost:5163"
```

Depois abra o Swagger:

```text
http://localhost:5163/swagger
```

Endpoint de verificação:

```text
http://localhost:5163/health
```

---

### 6. Correr o frontend

Pode abrir diretamente:

```text
frontend/index.html
```

Ou usar:

```text
start-frontend.bat
```

O frontend está preparado para consumir a API em:

```text
http://localhost:5163
```

---

## Utilizador inicial

Quando a API inicia, cria automaticamente um utilizador inicial:

```text
Email: admin@powerchord.com
Password: 123456
```

Este utilizador pode ser usado para fazer login e testar endpoints protegidos com JWT.

---

## Configuração

A configuração principal está em:

```text
PowerChordAPI/appsettings.json
```

Exemplo:

```json
{
  "ConnectionStrings": {
    "DefaultConnection": ""
  },
  "Jwt": {
    "Key": "change_this_super_secret_key_123456789_very_secure",
    "Issuer": "PowerChordAPI",
    "Audience": "PowerChordClient"
  },
  "Redis": {
    "ConnectionString": "localhost:6379,abortConnect=false"
  },
  "ExternalServices": {
    "PaymentsBaseUrl": "http://localhost:3000"
  }
}
```

### Base de dados em memória

Por defeito, esta versão corre com base de dados em memória:

```json
"ConnectionStrings": {
  "DefaultConnection": ""
}
```

Isto facilita a execução sem instalar SQL Server. Os dados são recriados quando a API reinicia.

### SQL Server opcional

Se quiser usar SQL Server LocalDB ou SQL Server Express, altere a connection string.

Exemplo com LocalDB:

```json
"ConnectionStrings": {
  "DefaultConnection": "Server=(localdb)\\MSSQLLocalDB;Database=PowerChordDB;Trusted_Connection=True;TrustServerCertificate=True;"
}
```

Exemplo com SQL Server Express:

```json
"ConnectionStrings": {
  "DefaultConnection": "Server=.\\SQLEXPRESS;Database=PowerChordDB;Trusted_Connection=True;TrustServerCertificate=True;"
}
```

A API usa Entity Framework Core e cria a base de dados/tabelas automaticamente com `EnsureCreated()`.

---

## Endpoints principais

### Autenticação

| Método | Endpoint | Protegido | Descrição |
|---|---|---:|---|
| POST | `/api/Auth/register` | Não | Regista um utilizador |
| POST | `/api/Auth/login` | Não | Faz login e devolve token JWT |
| GET | `/api/Auth/me` | Sim | Devolve dados do utilizador autenticado |

### Concertos

| Método | Endpoint | Protegido | Descrição |
|---|---|---:|---|
| GET | `/api/Concert` | Não | Lista concertos, usando cache local + Redis |
| GET | `/api/Concert/{id}` | Não | Consulta um concerto por ID |
| POST | `/api/Concert` | Sim | Cria um concerto |
| PUT | `/api/Concert/{id}` | Sim | Atualiza um concerto |
| DELETE | `/api/Concert/{id}` | Sim | Apaga um concerto |

### Bilhetes

| Método | Endpoint | Protegido | Descrição |
|---|---|---:|---|
| POST | `/api/Ticket` | Sim | Compra bilhete e chama o imposter de pagamentos |
| GET | `/api/Ticket` | Sim | Lista bilhetes |
| GET | `/api/Ticket/{id}` | Sim | Consulta um bilhete por ID |
| DELETE | `/api/Ticket/{id}` | Sim | Apaga um bilhete |

### Inventário

| Método | Endpoint | Protegido | Descrição |
|---|---|---:|---|
| GET | `/api/Inventory/{sku}` | Não | Consulta inventário simulado no Mountebank |

### Sistema

| Método | Endpoint | Descrição |
|---|---|---|
| GET | `/health` | Verifica se a API está ativa |

---

## Como testar no Swagger

### 1. Fazer login

No Swagger, execute:

```http
POST /api/Auth/login
```

Body:

```json
{
  "email": "admin@powerchord.com",
  "password": "123456"
}
```

A resposta devolve um token JWT.

### 2. Autorizar no Swagger

Clique no botão **Authorize** e escreva:

```text
Bearer TOKEN_AQUI
```

Depois disso, já pode testar os endpoints protegidos.

---

## Exemplo de registo

```http
POST /api/Auth/register
Content-Type: application/json
```

```json
{
  "email": "teste@powerchord.com",
  "password": "123456"
}
```

---

## Exemplo de login

```http
POST /api/Auth/login
Content-Type: application/json
```

```json
{
  "email": "teste@powerchord.com",
  "password": "123456"
}
```

Resposta esperada:

```json
{
  "token": "eyJhbGciOi..."
}
```

---

## Exemplo de criação de concerto

Endpoint protegido. Precisa de JWT.

```http
POST /api/Concert
Authorization: Bearer TOKEN_AQUI
Content-Type: application/json
```

```json
{
  "name": "Power Chord Final Show",
  "location": "Lisboa",
  "date": "2026-06-01T21:00:00",
  "price": 25
}
```

---

## Exemplo de compra de bilhete

Endpoint protegido. Precisa de JWT e do Mountebank ativo em `localhost:3000`.

```http
POST /api/Ticket
Authorization: Bearer TOKEN_AQUI
Content-Type: application/json
```

```json
{
  "concertId": 1,
  "quantity": 2
}
```

A API chama o endpoint simulado:

```text
POST http://localhost:3000/payments
```

Se o imposter responder com sucesso, o bilhete é registado.

---

## Imposter Mountebank

O ficheiro de configuração está em:

```text
imposter/mountebank.json
```

Serviços simulados:

| Método | URL | Descrição |
|---|---|---|
| POST | `http://localhost:3000/payments` | Simula pagamento aprovado |
| GET | `http://localhost:3000/inventory/{sku}` | Simula inventário disponível |

---

## Redis e cache

O endpoint `GET /api/Concert` usa uma estratégia de cache em camadas:

1. Primeiro tenta obter dados da cache local (`IMemoryCache`)
2. Se não existir, tenta obter dados do Redis
3. Se também não existir, consulta a base de dados
4. Atualiza a cache local e o Redis
5. Devolve JSON ao cliente

Se o Redis estiver desligado, a API continua a funcionar com cache local e base de dados.

---

## Polly e resiliência

A API usa Polly nas chamadas HTTP ao imposter de pagamentos/inventário.

Foram configurados:

- `RetryAsync(3)`: tenta novamente em caso de falha temporária
- `CircuitBreakerAsync(2, 30s)`: abre o circuito após falhas consecutivas para evitar sobrecarga

Isto é usado nos endpoints que comunicam com serviços externos simulados.

---

## Postman

A coleção Postman está em:

```text
postman/PowerChordAPI.postman_collection.json
```

Para usar:

1. Abrir Postman
2. Importar a coleção
3. Garantir que a API está ativa em `http://localhost:5163`
4. Fazer login
5. Copiar o token JWT
6. Usar o token nos endpoints protegidos

---

## Testes automáticos

Os testes estão em:

```text
tests/PowerChordAPI.Tests/
```

Para executar:

```powershell
cd tests\PowerChordAPI.Tests
dotnet test
```

---

## Scripts SQL

Os scripts estão em:

```text
database/schema.sql
database/seed.sql
```

Podem ser usados se quiser criar a base de dados manualmente no SQL Server.

A API também consegue criar as tabelas automaticamente através do Entity Framework Core.

---

## Ordem recomendada para apresentar/testar

1. Abrir o projeto no Visual Studio ou terminal
2. Iniciar o Mountebank com `start-mountebank.bat`
3. Iniciar Redis, se disponível
4. Iniciar a API com `start-api.bat`
5. Abrir Swagger em `http://localhost:5163/swagger`
6. Testar `GET /health`
7. Testar `GET /api/Concert`
8. Fazer login com `admin@powerchord.com` / `123456`
9. Autorizar no Swagger com JWT
10. Criar concerto
11. Comprar bilhete
12. Testar inventário com `/api/Inventory/TSHIRT-001`
13. Abrir o frontend

---

## Observações importantes

- Esta versão não precisa de Docker.
- A base de dados em memória é suficiente para demonstração local rápida.
- Para cumprir uma demonstração mais completa, recomenda-se usar SQL Server LocalDB/Express e Redis local.
- O Mountebank deve estar ativo para testar compra de bilhetes e inventário.
- A chave JWT do `appsettings.json` é apenas para ambiente de desenvolvimento.

---

## Autor

Projeto desenvolvido por Ricardo Chambel e Ivan Abasov para a tarefa final de criação de API REST consumida por Website / Aplicação Móvel.
