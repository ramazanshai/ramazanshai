from flask import Blueprint

api_blueprint = Blueprint('api', __name__, url_prefix='/api')

from .auth_routes import *
from .course_routes import *
from .lesson_routes import *
from .progress_routes import *

__all__ = ['api_blueprint']