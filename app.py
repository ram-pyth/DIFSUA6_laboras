from flask import Flask, render_template, request, redirect, url_for
from config import Config
from models import db, Projektas, AtliktasDarbas

app = Flask(__name__)
app.config.from_object(Config)

db.init_app(app)

# db paleidimo, lentelių sukūrimo kodas
with app.app_context():
    db.create_all()


###############################
# CRUD app
###############################

###############################
# R read
###############################

@app.route("/")
def show_all_rows():
    """
    List view -  sąrašo rodinys
    """
    search_text = request.args.get("paieska")
    if search_text:
        all_rows = Projektas.query.filter(Projektas.pavadinimas.ilike("%" + search_text + "%")).all()
    else:
        all_rows = Projektas.query.all()
    return render_template('index.html', all_rows=all_rows)


@app.route("/projektai/<int:projekto_id>", methods=['POST', 'GET'])
def show_one_project(projekto_id):
    """
    Detail view - vienos eilutės(vieno projekto)
    rodinys
    """
    one_project_row = Projektas.query.get(projekto_id)
    if not one_project_row:
        return f"Blogas id, projektas id {projekto_id} neegzistuoja"

    if request.method == 'POST':
        darbas = request.form.get('darbas')
        samata = request.form.get('samata')
        imone = request.form.get('imone')
        if darbas and samata and imone:
            atliktas_darbas = AtliktasDarbas(darbas=darbas, samata=samata, imone=imone)
            atliktas_darbas.projektas = one_project_row
            db.session.add(atliktas_darbas)
            db.session.commit()
    return render_template('one_project.html', one_project_row=one_project_row)

###############################
# C create
###############################

@app.route("/new", methods=['POST', 'GET'])
def create_new_project():
    if request.method == 'GET':
        return render_template('new_project.html')
    elif request.method == 'POST':
        pavadinimas = request.form.get('pavadinimas')
        plotas = request.form.get('plotas')
        kaina = request.form.get('kaina')
        if pavadinimas and plotas and kaina:
            new_project = Projektas(pavadinimas=pavadinimas, plotas=plotas, kaina=kaina)
            db.session.add(new_project)
            db.session.commit()
    return redirect(url_for("show_all_rows"))  # show_all_rows - homepage funkcijos pavadinimas


###############################
# D - delete
###############################
@app.route("/projektai/delete/<int:projekto_id>", methods=['POST'])
def delete_project(projekto_id):
    one_project_row = Projektas.query.get(projekto_id)
    if one_project_row:
        db.session.delete(one_project_row)
        db.session.commit()
    return redirect(url_for("show_all_rows"))


###############################
# U - update
###############################
@app.route("/projektai/update/<int:projekto_id>", methods=['GET', 'POST'])
def update_project(projekto_id):
    one_project_row = Projektas.query.get(projekto_id)
    if not one_project_row:
        return f"Blogas id, projektas id {projekto_id} neegzistuoja"

    if request.method == 'GET':
        return render_template("edit_project.html", one_project_row=one_project_row)

    elif request.method == 'POST':
        pavadinimas = request.form.get('pavadinimas')
        plotas = request.form.get('plotas')
        kaina = request.form.get('kaina')
        if pavadinimas and plotas and kaina:
            one_project_row.pavadinimas = pavadinimas
            one_project_row.plotas = plotas
            one_project_row.kaina = kaina
            db.session.commit()
    return redirect(url_for("show_all_rows"))


if __name__ == '__main__':
    app.run(port=5013)
