from flask import jsonify


def error_400(err):
    return jsonify({"error": "Solicitud incorrecta", "descripcion": str(err)}), 400


def error_404(err):
    return jsonify({"error": "Recurso no encontrado", "descripcion": str(err)}), 404


def error_409(err):
    return jsonify(
        {
            "error": "Conflicto con el estado actual",
            "descripcion": str(err),
        }
    ), 409


def error_422(err):
    return jsonify({"error": "Validación fallida", "descripcion": str(err)}), 422


def error_500(err):
    return jsonify(
        {"error": "Error interno del servidor", "descripcion": str(err)}
    ), 500


def register_error_handlers(app):
    """Registra los manejadores de error a nivel de aplicación.

    Los manejores declarados con @error_bp.errorhandler solo se aplicaban a
    las rutas del propio blueprint 'error', que no tiene rutas, por lo que
    nunca se ejecutaban y las respuestas de error salían en HTML.
    """
    app.errorhandler(400)(error_400)
    app.errorhandler(404)(error_404)
    app.errorhandler(409)(error_409)
    app.errorhandler(422)(error_422)
    app.errorhandler(500)(error_500)
