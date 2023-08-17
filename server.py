from flask import Flask, current_app
from flask_cors import CORS
from flask_restful_swagger_3 import swagger, get_swagger_blueprint

from views_blueprint import get_user_resources

app = Flask(__name__)
CORS(app, resources={"/api/*": {"origins": "*"}})


def auth(api_key, endpoint, method):
    # Space for your fancy authentication. Return True if access is granted, otherwise False
    return True


swagger.auth = auth

# Get user resources
user_resources = get_user_resources()

# Register the blueprint for user resources
app.register_blueprint(user_resources.blueprint)

# Prepare a blueprint to server the combined list of swagger document objects and register it
servers = [{"url": "http://localhost:5000"}]

SWAGGER_URL = '/api/doc'  # URL for exposing Swagger UI (without trailing '/')
API_URL = 'swagger.json'  # Our API url (can of course be a local resource)

# app.config.setdefault('SWAGGER_BLUEPRINT_URL_PREFIX', '/swagger')

swagger_blueprint = get_swagger_blueprint(
    user_resources.open_api_object,
    swagger_prefix_url=SWAGGER_URL,
    swagger_url=API_URL,
    title='Example', version='1', servers=servers)


app.register_blueprint(swagger_blueprint)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
