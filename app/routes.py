from app import app
from flask import render_template, flash, redirect, url_for, jsonify,json
from app.forms import LoginForm, AskPermission
import requests
from flask import request
import time


# 修饰器，会更改跟在其后的函数
@app.route('/')
@app.route('/index', methods=['GET', 'POST'])
def index():
    user = {'username': 'Miguel'}
    if request.method == "POST":
        company_id = request.args.get('companyID', type=str, default=None)
        print(company_id)
        print(request.url)
        company = {'companyID': company_id}
        print(company)
        return render_template('index.html', title='Home', user=user, company=company)
    return render_template('index.html', title='Home', user=user)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for user {}'.format(
            form.username.data
        ))
        permission_list1 = [{form.permission_list1.label: "001"},
                            {form.permission_list2.label: "002"},
                            {form.permission_list3.label: "003"}]
        permission_list = [
                            {permission_list1[0].get(form.permission_list1.label): form.permission_list1.data},
                            {permission_list1[1].get(form.permission_list2.label): form.permission_list2.data},
                            {permission_list1[2].get(form.permission_list3.label): form.permission_list3.data}]

        company_id = request.args.get('companyID', type=str, default=None)

        print(request.url)
        print("companyID", company_id)
        data = {"type": 0,
                "userID": form.username.data,
                "commonID": str(company_id),
                "boolean": permission_list,
                "timestamp": time.time(),
                }

        #r = requests.post("http://127.0.0.1:5001/userPermission.html", json=data)
        return jsonify(data)
        #return redirect('http://localhost:8080/index.jsp')
    return render_template('login.html', title='Sign In', form=form)


@app.route('/company', methods=['GET', 'POST'])
def company():
    form = AskPermission()
    if form.validate_on_submit():
        flash('Login requested for user {}'.format(
            form.username.data
        ))
        return jsonify(form.username.data)
    return render_template('company.html', title='Sign In', form=form)