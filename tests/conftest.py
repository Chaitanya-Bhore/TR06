import sqlite3

# Save the original sqlite3.connect function
_original_connect = sqlite3.connect

def mock_connect(*args, **kwargs):
    conn = _original_connect(*args, **kwargs)
    # Enable a 30-second busy timeout to handle concurrent write locks gracefully
    try:
        conn.execute("PRAGMA busy_timeout = 30000;")
    except sqlite3.OperationalError:
        pass
    return conn

# Monkeypatch sqlite3.connect globally for the test session
sqlite3.connect = mock_connect
