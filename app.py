from flask import Flask, request, render_template
from markupsafe import escape
import pandas as pd

app = Flask(__name__)

df_recipes = pd.read_parquet("assets/data/recipes.parquet.gzip")

@app.route("/")
def index():
   name = request.args.get("name", "Flask")
   return f"<p>Hello, {escape(name)}!</p>"

@app.route("/hello")
@app.route("/hello/<name>")
def hello_world(name=None):
   return render_template("index.html", person=name)

@app.route("/item/<string:item_name>")
def item(item_name):
   return f"<p>Hello, {escape(item_name)}!</p>"

@app.route("/recipes")
def recipes():
   return render_template("recipes.html", data=df_recipes)

@app.route("/recipes/nice")
def recipes_table():
   return render_template("data_table.html", title="Minecraft Recipes", data=df_recipes)

if __name__ == "__main__":
   app.run(debug=True)