# i dont't know why jinja also considers the lines which are commented out in html files so beaware
# https://github.com/saltstack/salt/issues/29543
# even comments like this form " <!--  --> "

from flask import Flask, render_template, request
from flask_mail import Mail, Message

app = Flask(__name__)

mail = Mail(app)

app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = 'vivekgameloop@gmail.com'
app.config['MAIL_PASSWORD'] = 'hbzw jmzt bgxn ooux'

app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True

mail = Mail(app)

SSL_DISABLE = True


@app.route('/')
def student():
    return render_template('index.html')


@app.route('/result', methods=['POST', 'GET'])
def result():
    if request.method == 'POST':
        result = request.form

        # code for mail sender
        subjectm = request.form.get('subject', type=str)
        reciptantm = request.form.get('toname')
        bodym = request.form.get('bodyemail', type=str)
        msg = Message(subject=subjectm, recipients=[reciptantm],
                      body=bodym, sender='vivekgameloop@gmail.com')

        # code for file sender

        # with app.open_resource('C:/Users/VIVEK/OneDrive/Languages_i_Completed/Python_udemy/Flask_email_sender_project/file.pdf') as file:
        #     msg.attach('file.pdf', 'application/pdf', file.read())

        uploaded_file = request.files['fileinput']
        msg.attach(uploaded_file.filename, uploaded_file.mimetype, uploaded_file.read())

        mail.send(msg)

        # msg = Message('heelopart2',sender='vivek04at3i@gmail.com',recipients=)
        mail.send(msg)

        return render_template('result.html', result=result)


if __name__ == '__main__':
    app.run(debug=True)


# student.html :
"""

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>61 flask request form object</title>
</head>
<body>
    <form action="https://localhost:5000/result" method="POST">
        <p>Name : </p>
        <p><input type="text" name="Name" /></p>
        <p>Physics : </p>
        <p><input type="text" name="Physics" /></p>
        <p>Chemistry : </p>
        <p><input type="text" name="chemistry" /></p>
        <p>Maths : </p>
        <p><input type="text" name="Mathematics" /></p>
        <p><input type="submit" value="Submit" /></p>
    </form>
</body>
</html>

"""


# result.html :
"""

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>61 result html</title>
</head>
<body>
    <table border="1">
        {% for key,value in result.iteritems() %}
        <tr>
            <th>{{ key }}</th>
            <th>{{ value }}</th>
        </tr>
        {% endfor %}
    </table>
</body>
</html>

"""


# errors you might encounter :
"""

 <!-- the below line gives error cause iteritemsis removed form python 3 instead dict.items  was give -->
 <!-- https://stackoverflow.com/questions/30418481/error-dict-object-has-no-attribute-iteritems -->
 <!-- {% for key,value in result.iteritems() %} -->



 <!-- https://stackoverflow.com/questions/56300832/jinja2-templatesyntaxerror-unexpected-end-of-template-jinja-was-looking-for?answertab=trending#tab-top -->


"""
