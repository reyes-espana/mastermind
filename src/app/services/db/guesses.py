from tabulate import tabulate
import sqlite3


con = sqlite3.connect("guesses.db")
cur = con.cursor()


def exists():
    sql = "SELECT name FROM sqlite_master WHERE type='table' AND name='guesses'"
    return bool(cur.execute(sql).fetchone())

def insert(guess, correct, close):
    cur.execute("INSERT INTO guesses(guess, correct, close) VALUES(?, ?, ?)", (str(guess)[1:-1], correct, close))
    return

def reset():
    cur.execute("DROP TABLE IF EXISTS guesses")
    cur.execute("CREATE TABLE guesses(guess, correct, close)")
    return

def store(guess, correct, close):
    if exists():
        insert(guess, correct, close)
    else: 
        reset()
        insert(guess, correct, close)
    return       

def view_all():
    res = cur.execute("SELECT * FROM guesses")
    data = [row for row in res]
    guesses = tabulate(data, headers=["Guess", "Correct", "Close"], tablefmt="grid")
    return guesses
