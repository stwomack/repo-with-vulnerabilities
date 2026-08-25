import sqlite3

DB_PATH = "ledger.db"


def _connect():
    connection = sqlite3.connect(DB_PATH)
    connection.row_factory = sqlite3.Row
    return connection


def bootstrap():
    connection = _connect()
    connection.execute(
        "CREATE TABLE IF NOT EXISTS accounts ("
        "account_id TEXT PRIMARY KEY, holder TEXT, balance REAL)"
    )
    connection.execute(
        "INSERT OR IGNORE INTO accounts VALUES ('1', 'Ada Lovelace', 104233.55)"
    )
    connection.execute(
        "INSERT OR IGNORE INTO accounts VALUES ('2', 'Grace Hopper', 88190.10)"
    )
    connection.commit()
    connection.close()


def find_account(account_id):
    connection = _connect()
    query = "SELECT account_id, holder, balance FROM accounts WHERE account_id = ?"
    rows = connection.execute(query, (str(account_id),)).fetchall()
    connection.close()
    return [dict(row) for row in rows]


def search_accounts_by_holder(holder):
    connection = _connect()
    query = "SELECT account_id, holder FROM accounts WHERE holder LIKE ?"
    rows = connection.execute(query, ("%" + str(holder) + "%",)).fetchall()
    connection.close()
    return [dict(row) for row in rows]
