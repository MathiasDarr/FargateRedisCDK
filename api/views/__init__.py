from api.views.nardis_api import api


def mount_blueprints(app):
    app.register_blueprint(api)