from functools import wraps

from flask import (
    session,
    redirect,
    url_for,
    flash
)


# =========================================
# ADMIN LOGIN REQUIRED
# =========================================
def admin_login_required(f):

    @wraps(f)
    def decorated_function(*args, **kwargs):

        if 'admin_id' not in session:

            flash(
                'Please Login First',
                'warning'
            )

            return redirect(
                url_for(
                    'admin.admin_login'
                )
            )

        return f(*args, **kwargs)

    return decorated_function


# =========================================
# CUSTOMER LOGIN REQUIRED
# =========================================
def customer_login_required(f):

    @wraps(f)
    def decorated_function(*args, **kwargs):

        if 'customer_id' not in session:

            flash(
                'Please Login First',
                'warning'
            )

            return redirect(
                url_for('web.login')
            )

        return f(*args, **kwargs)

    return decorated_function


# =========================================
# SUPER ADMIN REQUIRED
# =========================================
def super_admin_required(f):

    @wraps(f)
    def decorated_function(*args, **kwargs):

        if 'admin_id' not in session:

            flash(
                'Please Login First',
                'warning'
            )

            return redirect(
                url_for(
                    'admin.admin_login'
                )
            )

        # ROLE CHECK
        if session.get(
            'admin_role'
        ) != 'super_admin':

            flash(
                'Access Denied',
                'danger'
            )

            return redirect(
                url_for(
                    'admin.admin_dashboard'
                )
            )

        return f(*args, **kwargs)

    return decorated_function


# =========================================
# STAFF OR SUPER ADMIN
# =========================================
def staff_admin_required(f):

    @wraps(f)
    def decorated_function(*args, **kwargs):

        if 'admin_id' not in session:

            flash(
                'Please Login First',
                'warning'
            )

            return redirect(
                url_for(
                    'admin.admin_login'
                )
            )

        allowed_roles = [

            'super_admin',

            'staff'
        ]

        if session.get(
            'admin_role'
        ) not in allowed_roles:

            flash(
                'Access Denied',
                'danger'
            )

            return redirect(
                url_for(
                    'admin.admin_dashboard'
                )
            )

        return f(*args, **kwargs)

    return decorated_function