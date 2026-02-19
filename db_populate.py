from app import app, db, Projektas, AtliktasDarbas
import datetime

PROJECTS = [
    {"pavadinimas": "Ąžuolų Namai", "plotas": "120", "kaina": 85},
    {"pavadinimas": "Saulės Rezidencija", "plotas": "150", "kaina": 120},
    {"pavadinimas": "Neries Panorama", "plotas": "180", "kaina": 160},
    {"pavadinimas": "Pušų Terasos", "plotas": "210", "kaina": 210},
    {"pavadinimas": "Miško Apartamentai", "plotas": "250", "kaina": 260},
    {"pavadinimas": "Senamiesčio Loftai", "plotas": "300", "kaina": 320},
    {"pavadinimas": "Parko Kvartalas", "plotas": "350", "kaina": 390},
    {"pavadinimas": "Vilnelės Namai", "plotas": "400", "kaina": 470},
    {"pavadinimas": "Centro Apartamentai", "plotas": "450", "kaina": 550},
    {"pavadinimas": "Ežero Rezidencija", "plotas": "500", "kaina": 630},
    {"pavadinimas": "Kalnų Panorama", "plotas": "600", "kaina": 760},
    {"pavadinimas": "Jūros Vilos", "plotas": "700", "kaina": 890},
    {"pavadinimas": "Smėlio Terasa", "plotas": "800", "kaina": 1020},
    {"pavadinimas": "Beržų Slėnis", "plotas": "900", "kaina": 1180},
    {"pavadinimas": "Upės Apartamentai", "plotas": "1000", "kaina": 1350},
    {"pavadinimas": "Naujamiesčio Projektas", "plotas": "1100", "kaina": 1500},
    {"pavadinimas": "Vilniaus Vartai", "plotas": "1200", "kaina": 1680},
    {"pavadinimas": "Baltic Residence", "plotas": "1300", "kaina": 1850},
    {"pavadinimas": "Amber City Namai", "plotas": "1400", "kaina": 2050},
    {"pavadinimas": "Green Park Kvartalas", "plotas": "1500", "kaina": 2200},
    {"pavadinimas": "River View Apartamentai", "plotas": "1600", "kaina": 2350},
    {"pavadinimas": "Sunset Panorama", "plotas": "1700", "kaina": 2500},
    {"pavadinimas": "Nordic Loftai", "plotas": "1750", "kaina": 2600},
    {"pavadinimas": "Imperial Rezidencija", "plotas": "1800", "kaina": 2700},
    {"pavadinimas": "Grand Vilnius Namai", "plotas": "1850", "kaina": 2800},
    {"pavadinimas": "Harmony Park Projektas", "plotas": "1900", "kaina": 2850},
    {"pavadinimas": "Elite City Terasos", "plotas": "1950", "kaina": 2900},
    {"pavadinimas": "Royal Gardens Residence", "plotas": "1980", "kaina": 2950},
    {"pavadinimas": "Prestige Panorama", "plotas": "1990", "kaina": 2980},
    {"pavadinimas": "Capital Grand Kvartalas", "plotas": "2000", "kaina": 3000},
]


def populate():
    # Optional: clear old data
    # db.session.query(Projektas).delete()
    project_rows = []
    for data in PROJECTS:
        projektas = Projektas(
            pavadinimas=data["pavadinimas"],
            plotas=data["plotas"],
            kaina=data["kaina"]
            # ivedimo_data=datetime.datetime.now()
        )
        project_rows.append(projektas)

    project1: Projektas = project_rows[0]
    project1.atlikti_darbai.extend(
        [AtliktasDarbas(darbas="Langų sudėjimas", samata=45000, imone="Litlanga"),
         AtliktasDarbas(darbas="Šaligatvis", samata=60000, imone="Litplyta"),
         AtliktasDarbas(darbas="Stogas", samata=70000, imone="Litstoga")]
    )

    project2: Projektas = project_rows[1]
    project2.atlikti_darbai.extend(
        [AtliktasDarbas(darbas="Vitražinių langų sudėjimas", samata=45000, imone="Pollanga"),
         AtliktasDarbas(darbas="Šaligatvis", samata=50000, imone="Litplyta"),
         AtliktasDarbas(darbas="Stogas", samata=55000, imone="Litstoga"),
         AtliktasDarbas(darbas="Registras", samata=5000, imone="Registro karaliai")]
    )

    db.session.add_all(project_rows)
    db.session.commit()
    print("Database populated with predefined project data.")


if __name__ == "__main__":
    with app.app_context():
        populate()
