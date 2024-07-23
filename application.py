from flask import Flask, render_template, request
from models import *

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://postgres:trinhthanhtung30@127.0.0.1:5432/postgres"
app.config["SQLALCGEMY_TRACK_MODIFICATIONS"] = False
db.init_app(app)

@app.route('/website')
def Website():
    return render_template('website.html')  
# I COMMODITY

@app.route('/website_commodity' )
def website_commodity():
    return render_template('website_commodity.html')
# 1 Info commodity 
@app.route('/info_commodity')
def info_commodity():
    commoditys = Commodity.query.all()
    return render_template('info_commodity.html', commoditys=commoditys)
# 2 Add commodity
@app.route('/add_commodity')
def add_commodity():
    return render_template('add_commodity.html')

@app.route('/add_commodity_success')
def add_commodity_success():
    commodity_codes = request.args.get("commodity_codes")
    goods_name = request.args.get("goods_name")
    year_of_manufacture = request.args.get("year_of_manufacture")
    product_price = request.args.get("product_price")
    note = request.args.get("note")
    company_codes = request.args.get("company_codes")
    commoditys = Commodity(commodity_codes=commodity_codes, goods_name=goods_name,\
        year_of_manufacture=year_of_manufacture,product_price=product_price,note=note, company_codes=company_codes)
    db.session.add(commoditys)
    db.session.commit()
    return render_template('add_commodity_success.html')
# 3 Update Commodity
@app.route('/update_commodity')
def update_commodity():
    commoditys = Commodity.query.all()
    return render_template("update_commodity.html", commoditys=commoditys)

@app.route('/update_commodity_success')
def update_commodity_success():
    commodity_codes = request.args.get("commodity_codes")
    commoditys = Commodity.query.get(commodity_codes)
    commoditys.goods_name = request.args.get("goods_name")
    commoditys.year_of_manufacture = request.args.get("year_of_manufacture")
    commoditys.product_price = request.args.get("product_price")
    commoditys.note = request.args.get("note")
    commoditys.company_codes = request.args.get("company_codes")
    db.session.commit()
    return render_template("update_commodity_success")

# 4 Delete commodity 

@app.route('/delete_commodity')
def delete_commodity():
    commoditys = Commodity.query.all()
    return render_template ("delete_commodity.html", commoditys=commoditys)

@app.route('/delete_commodity_success')
def delete_commodity_success():
    commodity_codes = request.args.get("commodity_codes")
    commoditys = Commodity.query.get(commodity_codes)
    db.session.delete(commoditys)
    db.session.commit()
    return render_template("delete_commodity_success.html")

# 5 Show commodity 
@app.route('/show_commodity')
def show_commodity():
    commoditys = Commodity.query.all()
    return render_template ("show_commodity.html", commoditys=commoditys)
    
@app.route('/show_commodity_success')
def show_commodity_success():
    commodity_codes = request.args.get("commodity_codes")
    commodity = Commodity.query.get(commodity_codes)
    return render_template("show_commodity_success.html", commodity=commodity)


# II COMPANY 
@app.route('/website_company')
def website_company():
    return render_template('website_company.html')
# 1 Info company 
@app.route('/info_company')
def info_company():
    companys = Company.query.all()
    return render_template ('info_company.html', companys=companys)

# 2 Add company 
@app.route('/add_company')
def add_company():
    return render_template('add_company.html')

@app.route('/add_company_success')
def add_company_success():
    company_code = request.args.get("company_code")
    company_name = request.args.get("company_name")
    founded_year = request.args.get("founded_year")
    company_address = request.args.get("company_address")
    companys =  Company(company_code=company_code, company_name=company_name,founded_year=founded_year,company_address=company_address)
    db.session.add(companys)
    db.session.commit()
    return render_template('add_company_success.html')

# 3 Update company 
@app.route('/update_company')
def update_company():
    companys = Company.query.all()
    return render_template("update_company.html", companys=companys)

@app.route('/update_company_success')  
def update_company_success():
    company_code = request.args.get("company_code")
    companys = Company.query.get(company_code)
    companys.company_name = request.args.get("company_name")
    companys.founded_year = request.args.get("founded_year")
    companys.company_address = request.args.get("company_address")
    db.session.add(companys)
    db.session.commit()
    return render_template ("update_company_success.html")

# 4 Delete company 

@app.route('/delete_company')
def delete_company():
    companys = Company.query.all()
    return render_template("delete_company.html", companys=companys)

@app.route('/delete_company_success')
def  delete_company_success():
    company_code = request.args.get("company_code")
    companys = Company.query.get(company_code)
    db.session.delete(companys)
    db.session.commit()
    return render_template("delete_company_success.html")

# 5 Show company 
@app.route('/show_company')
def show_company():
    companys = Company.query.all()
    return render_template("show_company.html", companys=companys)
    
@app.route('/show_company_success')
def show_company_success():
    company_code = request.args.get("company_code")
    company = Company.query.get(company_code)
    db.session.commit()
    return  render_template("show_company_success.html", company=company)
    

if __name__== '__main__':
    app.run(debug=True)
