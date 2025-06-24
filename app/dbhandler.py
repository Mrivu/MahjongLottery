import db

def get_leaderboard():
    sql = """SELECT username, seasonScore FROM users"""
    return db.query(sql, [])