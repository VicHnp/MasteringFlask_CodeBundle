from flask import Flask, render_template, Blueprint, redirect, url_for
from flask.views import MethodView

app = Flask(__name__)
app.debug=True

class HomeView(MethodView):
    def get(self, num=None):
        if not num:
            return 'abc'
        return num

app.add_url_rule(
    '/', view_func=HomeView.as_view('root')
)
app.add_url_rule(
    '/home/<string:num>', view_func=HomeView.as_view('home')
)

if __name__ == '__main__':
    app.run()