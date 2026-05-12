from flask import render_template


# =========================
# REGISTER ERROR HANDLERS
# =========================
def register_error_handlers(app):


    # =========================
    # 404 ERROR
    # =========================
    @app.errorhandler(404)
    def page_not_found(error):

        return render_template(
            'errors/404.html'
        ), 404


    # =========================
    # 500 ERROR
    # =========================
    @app.errorhandler(500)
    def internal_server_error(error):

        return render_template(
            'errors/500.html'
        ), 500