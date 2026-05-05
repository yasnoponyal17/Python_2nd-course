from jinja2 import Environment, FileSystemLoader, select_autoescape

env = Environment(
    loader=FileSystemLoader('templates'),
    autoescape=select_autoescape()
)

template_index = env.get_template("index.html")
template_author = env.get_template("author.html")



def index(author, app):
        return template_index.render(
 			author_name=author.name,
 			group=author.group,
 			app_name=app.name,
 			navigation=[{'caption': 'Главная', 'href': '/'},
            			{'caption': 'Об авторе', 'href': '/author'},
               			{'caption': 'Курсы валют', 'href': '/currencies'},
						{'caption': 'Пользователи', 'href': '/users'}
              			]
		)
        
def author(author):
    return template_author.render(
    		author_name=author.name,
    		group=author.group
		)