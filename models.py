from flask_sqlalchemy import SQLAlchemy
import datetime

# db objektas
db = SQLAlchemy()

class Projektas(db.Model):  # type: ignore
    __tablename__ = 'nt_projektai'
    id = db.Column(db.Integer, primary_key=True)
    pavadinimas = db.Column(db.String)
    plotas = db.Column(db.Float)
    kaina = db.Column(db.Float)
    ivedimo_data = db.Column(db.DateTime, default=datetime.datetime.now)
    atlikti_darbai = db.relationship('AtliktasDarbas', backref='projektas', cascade='all, delete-orphan')

    # @property
    # def kaina(self):
    #     samatu_suma = sum([atliktas_darbas.samata for atliktas_darbas in self.atlikti_darbai]) / 1000
    #     return round(samatu_suma)

    @property
    def kaina_pvm(self):
        return round(self.kaina * 1.21, 2)

    @property
    def kv1_kaina(self):
        """
        1 kv metro kaina
        BE PVM
        """
        return round(self.kaina * 1000 / self.plotas, 2)

    def __str__(self):
        return f"{self.id} {self.pavadinimas} {self.plotas} {self.kaina} {self.ivedimo_data}"


class AtliktasDarbas(db.Model):
    __tablename__ = 'atlikti_darbai'
    id = db.Column(db.Integer, primary_key=True)
    darbas = db.Column(db.String)
    samata = db.Column(db.Float)
    imone = db.Column(db.String)
    projektas_id = db.Column(db.Integer, db.ForeignKey('nt_projektai.id'), nullable=False)
    # projektas = nereikia, nes jis sukuriamas Projektas klasėje per atlikti_darbai .. backref='projektas'

    def __str__(self):
        return f"{self.id} {self.darbas} {self.samata} {self.imone}"
