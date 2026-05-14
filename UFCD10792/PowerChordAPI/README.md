# PowerChordAPI

API REST em **ASP.NET Core 8** para gestão de concertos e venda de bilhetes da banda fictícia **Power Chord**.

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

## Requisitos para correr sem Docker

Obrigatório:

- **.NET SDK 8**
- **Node.js**, para correr o Mountebank com `npx`

Opcional:

- **Redis para Windows**, Memurai, Redis via WSL, ou outro servidor Redis local
- **SQL Server LocalDB / SQL Server Express**, caso não queira usar a base de dados em memória
- **Postman**, para importar a coleção de testes

> A API corre mesmo sem SQL Server configurado, porque usa `InMemoryDatabase` quando `ConnectionStrings:DefaultConnection` está vazio.
