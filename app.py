from flask import Flask


from think.library.build import Build
Build().run()
app = Flask(__name__)



if __name__ == '__main__':
    app.run()
