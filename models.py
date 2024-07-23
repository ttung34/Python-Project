from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Commodity(db.Model):
    __tablename__ = "commodity"
    commodity_codes = db.Column(db.Integer, primary_key = True)
    goods_name = db.Column(db.String, nullable = False)
    year_of_manufacture = db.Column(db.Date, nullable = False)
    product_price = db.Column(db.Integer, nullable = False)
    note = db.Column(db.String, nullable = False)
    company_codes = db.Column(db.String, db.ForeignKey("company.company_code"), nullable = False)
    
class Company(db.Model):
    __tablename__ = "company"
    company_code = db.Column(db.String, primary_key = True)
    company_name = db.Column(db.String, nullable = False)
    founded_year = db.Column(db.Date, nullable = False)
    company_address = db.Column(db.String, nullable = False)
    