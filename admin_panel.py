from flask import Blueprint

admin = Blueprint('admin', __name__)

@admin.get('/admin')
def dashboard():
    return 'Admin panel coming soon'
