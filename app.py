from flask import Flask
app=Flask(__name__)
@app.route('/',methods=['GET','POST'])
def index():
    return "WELCOME TO THE ML CLASS"

if __name__ == '__main__':
    app.run(debug=True)


## heroku email chaturvedihimanshu120@gmail.com
## heroku api key = 9db712fc-8051-4f84-8387-a4302dba93b8
## heroku app name = 