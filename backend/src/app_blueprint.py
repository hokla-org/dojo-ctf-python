from flask import Blueprint, Flask, make_response

# Crée un objet Blueprint
app_blueprint = Blueprint('app_blueprint', __name__)

def get_flag():
    # La logique pour obtenir le drapeau va ici
    flag_content = "Contenu du drapeau"  # Remplace par la valeur réelle du drapeau

    # Crée une réponse Flask avec le contenu du drapeau
    response = make_response(flag_content)

    # Ajoute les en-têtes nécessaires (par exemple, pour gérer le format de la réponse)
    response.headers['Content-Type'] = 'text/plain'

    return response

# Enregistre la route dans le blueprint
app_blueprint.add_url_rule('/flag', view_func=get_flag)







