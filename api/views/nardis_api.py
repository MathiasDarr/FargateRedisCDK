from flask import Blueprint, request, jsonify, current_app
import logging

api = Blueprint("collections_api", __name__)
log = logging.getLogger()


@api.route('/')
def index():
    return "helloadda"
