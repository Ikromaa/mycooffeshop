from flask import render_template, redirect, url_for, flash, request
from flask_login import login_user, logout_user, login_required, current_user
from app import app, db, login_manager
from app.forms import ReservationForm, RegistrationForm, LoginForm
from app.models import User, Reservation

# Home page
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(username=form.username.data, email=form.email.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('Registration successful. You can now log in.', 'success')
        return redirect(url_for('login'))
    
    return render_template('register.html', form=form)

# Login page
@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))

    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and user.check_password(form.password.data):
            login_user(user)
            next_page = request.args.get('next')
            return redirect(next_page or url_for('index'))
        else:
            flash('Invalid email or password. Please try again.', 'danger')
    
    return render_template('login.html', form=form)

# Logout route
@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('index'))

# Profile page
@app.route('/profile')
@login_required
def profile():
    user = current_user
    user_reservations = user.reservations
    return render_template('profile.html', user=user, reservations=user_reservations)

# Booking page
@app.route('/book', methods=['GET', 'POST'])
@login_required
def book():
    form = ReservationForm()
    if form.validate_on_submit():
        reservation = Reservation(
            name=form.name.data,
            email=form.email.data,
            date=form.date.data,
            time=form.time.data,
            user_id=current_user.id
        )
        db.session.add(reservation)
        db.session.commit()
        flash('Reservation successful!', 'success')
        return redirect(url_for('reservation_detail', reservation_id=reservation.id))
    return render_template('book.html', form=form)

# Reservation detail page
@app.route('/reservation/<int:reservation_id>')
@login_required
def reservation_detail(reservation_id):
    reservation = Reservation.query.get_or_404(reservation_id)
    return render_template('reservation_detail.html', reservation=reservation)

# Reservation cancel

@app.route('/cancel_reservation/<int:reservation_id>', methods=['POST'])
@login_required
def cancel_reservation(reservation_id):
    reservation = Reservation.query.get_or_404(reservation_id)

    # Verifikasi bahwa pengguna yang membatalkan reservasi adalah pemilik reservasi
    if current_user.id != reservation.user_id:
        flash('You are not authorized to cancel this reservation.', 'danger')
        return redirect(url_for('profile'))

    db.session.delete(reservation)
    db.session.commit()

    flash('Reservation canceled successfully!', 'success')
    return redirect(url_for('profile'))