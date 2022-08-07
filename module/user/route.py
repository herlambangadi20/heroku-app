from flask import Blueprint, render_template
from common.Database import Connection

user_bp=Blueprint(
    'user_bp',
    __name__,
)

class model(Connection):
    def coba(self):
        self.connect()
        result = self.conn.executeQuery('select * from account')
        self.disconnect()
        print(result[0])
        return result[0]

# ---------- route
@user_bp.get('/')
def index(**kwargs):
    return str(model().coba())