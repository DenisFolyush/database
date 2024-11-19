# app/my_project/auth/route/route.py

from app.my_project.auth.controller.controller import controller


def register_routes(app):
    """
    Реєструє всі маршрути додатку.
    """
    app.register_blueprint(controller, url_prefix='/api')
