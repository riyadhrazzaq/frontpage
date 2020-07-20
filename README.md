# yellow
A small portfolio app built with Flask and Bootstrap.

# Configure and Run
```
git clone https://github.com/riyadhrazzaq/yellow.git
cd yellow
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python app.py
```

# Create Your Portfolio
## Basic
Current structure of the project is,
```
frontpage/
	content/
		project/
			somefile.json
			anotherfile.json
		publication/
			someproject.json
			anotherproject.json
	static/
	templates/
	app.py
	config.py
	requirements.txt
```

`content/` folder is the backbone of this site. This is where project/publications and other stuff lives. For each section in the site such as **Works, Publication** etc, it needs a folder by that name. Inside them, each project files are stored in [JSON](http://www.json.org/example.html) file. Each project will have its own file. Any JSON file may have following properties, 
* `title`: TEXT. The title of your project.
* `description`: TEXT. Description of your project.
* `date`: TEXT. Date of your project. Formatting must be done by yourself.
* `image`: URL. One image URL accompanying the project. If you store images locally, it must be inside `static/`
* 'more': URL. It will be added to the "More" button. For example, if your project is stored in a [Kaggle](www.kaggle.com) notebook, then URL can be of that notebook.
* `tools`: LIST. A list of tools, frameworks etc used in your project. 

You may add or remove some of them, which may work or might lead to chaos, I have not tested yet.

In `config.py`, Change `ME`, `TITLE` and other social-media variables in `SOCIAL`. In, `SOCIAL`, accompanying every URL, there are some variables like `fab fa-twitter`. These are [FontAwesome](https://fontawesome.com/) icons which can be added optionally. Go to their website, copy and paste codes of the one you like.

## New Sections
New sections can be created just by creating a new folder inside `content/` and add the corresponding details in `SECTION` variable in `config.py`.

## Theme
Most of the design is done using [Bootstrap](https://getbootstrap.com/docs/4.5/getting-started/introduction/). Custom CSS are only used for fonts and `<hr>` customization. To begin customizing, look at how colors can be changed using Bootstrap, [LINK](https://getbootstrap.com/docs/4.5/utilities/colors/).

## Warnings
**JSON files needs character escaping.** For example, if you need double-quotes `""` in any text in JSON, you will need to add a single blackslash `\` before them. `He is the "The Dark Knight"` will become `He is \"The Dark Knight\"`