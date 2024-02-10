import urllib.request as urllib2
from bs4 import BeautifulSoup
from flask import Flask, render_template, flash
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["SECRET_KEY"] = "super-secret-key"  # Wymagane do flash()
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database.db"  # Ścieżka do pliku z bazą danych

db = SQLAlchemy(app)  # Obiekt bazy danych


class Dates(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    rate = db.Column(db.Integer)
    change = db.Column(db.Integer)
    change_percent = db.Column(db.Integer)
    number_of_transaction = db.Column(db.Integer)
    trading = db.Column(db.Integer)
    opening_rate = db.Column(db.Integer)
    max_rate = db.Column(db.Integer)
    min_rate = db.Column(db.Integer)
    date_time = db.Column(db.Integer)


with app.app_context():
    db.create_all()


@app.route("/")
def index():
    try:
        list_datas = Dates.query.all()
        return render_template("index.html", list_datas=list_datas)
    except:
        flash(f"błąd spróbuj ponownie")
        list_datas = Dates.query.all()
        return render_template("index.html", list_datas=list_datas)


URL = "https://www.bankier.pl/gielda/notowania/akcje"
page = urllib2.urlopen(URL)
soup = BeautifulSoup(page, 'html.parser')


def data(tag, class_name):
    name_box = soup.find_all(tag, attrs={'class': class_name})
    names = [link.get_text() for link in name_box]
    names_text = [element.strip() for element in names]
    return names_text


@app.route("/", methods=["POST"])
def scrap():
    try:
        name_text = data('td', 'colWalor textNowrap')
        name_text2 = data('td', 'colKurs')
        name_text6 = data('td', 'colZmiana')
        name_text7 = data('td', 'colZmianaProcentowa')
        name_text3 = data('td', 'colLiczbaTransakcji')
        name_text3 = [element.replace("\xa0", "") for element in name_text3]
        name_text4 = data('td', 'colObrot')
        name_text4 = [element.strip() for element in name_text4]
        name_text4 = [element.replace("\xa0", "") for element in name_text4]
        name_text5 = data('td', 'colOtwarcie')
        name_text5 = [element.strip() for element in name_text5]
        name_text5 = [element.replace("\xa0", "") for element in name_text5]
        name_text8 = data('td', 'calMaxi')
        name_text8 = [element.strip() for element in name_text8]
        name_text8 = [element.replace("\xa0", "") for element in name_text8]
        name_text9 = data('td', 'calMini')
        name_text9 = [element.strip() for element in name_text9]
        name_text9 = [element.replace("\xa0", "") for element in name_text9]
        name_text10 = data('td', 'colAktualizacja')
        name_text10 = [element.strip() for element in name_text10]
        name_text10 = [element.replace("\xa0", "") for element in name_text10]

        for i in range(len(name_text)):
            name = name_text[i]
            rate = name_text2[i]
            change = name_text6[i]
            change_percent = name_text7[i]
            number_of_transaction = name_text3[i]
            trading = name_text4[i]
            opening_rate = name_text5[i]
            max_rate = name_text8[i]
            min_rate = name_text9[i]
            date_time = name_text10[i]

            verify = db.session.query(Dates).filter_by(name=name, date_time=date_time).first()
            if verify is None:
                new_item = Dates(name=name, rate=rate, change=change, change_percent=change_percent,
                                 number_of_transaction=number_of_transaction, trading=trading,
                                 opening_rate=opening_rate, max_rate=max_rate, min_rate=min_rate, date_time=date_time)
                db.session.add(new_item)
        db.session.commit()
        list_datas = Dates.query.all()
        return render_template("index.html", list_datas=list_datas)

    except:
        flash(f"błąd spróbuj ponownie")
        list_datas = Dates.query.all()
        return render_template("index.html", list_datas=list_datas)

