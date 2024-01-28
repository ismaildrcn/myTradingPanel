import sqlite3 as sql


class Database():
    def __init__(self):
        self.connection = sql.connect('text.db')
        self.cursor = self.connection.cursor()
        self.createSymbolTable()

    def createSymbolTable(self):
        command = "CREATE TABLE IF NOT EXISTS symbols (id INTEGER PRIMARY KEY AUTOINCREMENT, symbol varchar(8) NOT NULL, screener varchar(16) NOT NULL, exchange varchar(32) NOT NULL)"
        self.cursor.execute(command)

    def addSymbol(self, symbol, screener, exchange, cost, lot):
        with self.connection:
            existing_record = self.checkQuery(symbol)
            if not existing_record:
                command = f"INSERT INTO symbols (symbol, screener, exchange, cost, lot) VALUES (?, ?, ?, ?, ?)"
                self.cursor.execute(command, (symbol, screener, exchange, cost, lot))
                self.connection.commit()
            else:
                print("Kayıt zaten var, tekrar eklenmedi.")

    def checkQuery(self, symbol):
        check_query = "SELECT 1 FROM symbols WHERE symbol = ? LIMIT 1"
        self.cursor.execute(check_query, (symbol,))
        return self.cursor.fetchone()
