CREATE TABLE users (
    userID INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT UNIQUE,
    password_hash TEXT,
    isAdmin INTEGER,
    seasonScore INTEGER
);
