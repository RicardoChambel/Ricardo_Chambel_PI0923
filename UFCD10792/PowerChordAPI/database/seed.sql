INSERT INTO Concerts (Name, Location, Date, Price)
VALUES
('Power Chord Live', 'Lisboa', '2026-06-01 21:00:00', 25.00),
('Power Chord Rock Night', 'Porto', '2026-07-15 22:00:00', 30.00),
('Power Chord Summer Tour', 'Coimbra', '2026-08-10 20:30:00', 20.00),
('Power Chord Gig', 'ESE Setúbal', '2026-04-16 20:30:00', 0.00);

-- Password: 123456
-- A API também cria este utilizador automaticamente se a tabela estiver vazia.
INSERT INTO Users (Email, PasswordHash)
VALUES
('admin@powerchord.com', '123456');
