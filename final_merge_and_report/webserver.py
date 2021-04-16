from flask import Flask, redirect, request, session, make_response

app = Flask(__name__)

app.secret_key = b'kevinelong'


@app.route('/')
def index():
    return "Hey <b>there</b>!<br><a href=\"/signup_form/\"> NEXT </a>"


@app.route('/reports/')
def reports():
    if "report" in request.args:
        r = request.args["report"]
        f = open(f"./output/{r}.json")
        response = make_response(f.read())
        response.headers['Content-Type'] = 'application/json'
        return response
    else:
        r = "None"
    return f"""

<a href="?report=by_date" style="outline:1px solid black;padding:1em;text-decoration:none">
    EMAIL GROUP BY DATE
</a>
<br><br><br><br>
<a href="?report=by_sender" style="outline:1px solid black;padding:1em;text-decoration:none">
    EMAIL GROUP BY SENDER
</a>
    """


@app.route('/signup_form/')
def signup_form():
    return '''
<html>
    <head>
        <title>Page Title</title>
    </head>
    <body>
    
        <h1>
            This is a Heading
        </h1>
        <p>
            This is a paragraph.
        </p>
        
        <form method="POST" action="/signup">
            <input name="email">
            <input type="submit">
        </form>
    
    </body>
</html>
'''


@app.route('/signup', methods=['POST'])
def signup():

    email = request.form['email']
    print(f"RECEIVED: {email}")

    f = open("mailing_list.txt", "a")
    f.write(f"{email} {request}\n")

    return redirect('/thanks/')


@app.route('/thanks/')
def thanks():
    return "Thanks for signing up! <a href=\"/\">home</a>"


@app.route('/secure_me/')
def secure_me():
    if "username" in dict(session):
        f = open("mailing_list.txt", "r")
        all = f.read()
        return all
    else:
        return "405"

@app.route('/login/')
def login():
    return '''
<form method="POST" action="/authenticate">
    <input name="username">
    <input name="password" type="password">
    <input type="submit">
</form>
'''

@app.route('/authenticate', methods=['POST'])
def authenticate():
    username = request.form['username']
    session["username"] = username
    return redirect('/content/')

@app.route('/content/')
def content():
    username = session["username"]
    return f'''
CONTENT<BR>
{username}
<a href="/secure_me/">
    Download Mailing List
</a>
'''

if __name__ == '__main__':
    app.run()
