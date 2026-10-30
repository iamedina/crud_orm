from flask import jsonify, request, abort
from sqlalchemy.exc import IntegrityError

from app.models import Categoria, db


# LISTAR CATEGORIAS
def categoria_list():
    categorias = db.session.execute(db.select(Categoria)).scalars().all()
    return jsonify([c.to_dict() for c in categorias]), 200


# DETALLE CATEGORIA
def categoria_detail(categoria_id):
    categoria = db.session.get(Categoria, categoria_id)
    if not categoria:
        abort(404, description="Categoría no encontrada")
    return jsonify(categoria.to_dict()), 200
    # CREAR CATEGORIA


def categoria_add():
    data = request.get_json()

    if not data:
        abort(400, description="No se recibió información en formato JSON")

    if "nombre" not in data:
        abort(400, description="El campo nombre es obligatorio")

    # Verificar que no exista otra categoría con el mismo nombre
    nombre = data["nombre"]
    existente = db.session.execute(
        db.select(Categoria).where(Categoria.categoria_nombre == nombre)
    ).scalar_one_or_none()

    if existente:
        abort(
            400,
            description=f"Ya existe una categoría con el nombre '{nombre}'",
        )

    nueva_categoria = Categoria(
        categoria_nombre=data["nombre"], descripcion=data.get("descripcion")
    )

    db.session.add(nueva_categoria)
    db.session.commit()

    return jsonify(nueva_categoria.to_dict()), 201

    # ACTUALIZAR CATEGORIA


def categoria_update(categoria_id):
    data = request.get_json()

    if not data:
        abort(400, description="No se recibió información en formato JSON")

    categoria = db.session.get(Categoria, categoria_id)
    if not categoria:
        abort(404, description="Categoría no encontrada")
    categoria.categoria_nombre = data.get("nombre", categoria.categoria_nombre)
    categoria.descripcion = data.get("descripcion", categoria.descripcion)

    db.session.commit()

    return jsonify(categoria.to_dict()), 200

    # ELIMINAR CATEGORIA


def categoria_delete(categoria_id):
    categoria = db.session.get(Categoria, categoria_id)
    if not categoria:
        abort(404, description="Categoría no encontrada")

    try:
        db.session.delete(categoria)
        db.session.commit()
    except IntegrityError:
        db.session.rollback()
        abort(
            409,
            description="No se puede eliminar la categoría: tiene productos asociados",
        )

    return jsonify({"mensaje": "Categoría eliminada correctamente"}), 200
