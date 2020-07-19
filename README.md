# yellow
A small portfolio app built with Flask and Bootstrap.
# Configure and Run
```
git clone https://github.com/riyadhrazzaq/yellow.git
cd yellow
python -m venv venv
pip install -r requirements.txt
python app.py
```

# Create Your Portfolio
```
assets/
	content/
templates/
app.py
config.py
```
`content/` is where each project files are stored in [JSON](http://www.json.org/example.html) file. Each project will have its own file. The JSON file has the following properties, 
* `title`: TEXT. The title of your project.
* `description`: TEXT. Description of your project.
* `date`: TEXT. Date of your project. Formatting must be done by yourself.
* `image`: URL. One image url accompanying the project. URL can be of imgur, postimage etc. 
* 'more': URL. It will be added to the "More" button. For example, if your project is stored in a [Kaggle](www.kaggle.com) notebook, then URL can be of that notebook.
* `tools`: LIST. A list of tools, frameworks etc  used in your project. 

Change `NAME` and other social-media variables in `config.py`. 

