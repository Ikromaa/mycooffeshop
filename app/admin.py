from app import db
from app.models import User
from werkzeug import generate_password_hash


admin = User(username='admin', email='mychoffeshop.com', is_admin=True)
admin.set.password('mychoffeshop123')
db.session.add(admin)
db.session.commit()

print('Akun admin sukses dibuat')