from jinja2 import Environment, FileSystemLoader, select_autoescape

env = Environment(
    loader=FileSystemLoader('templates'),
    autoescape=select_autoescape()
)

template_index = env.get_template("index.html")
template_author = env.get_template("author.html")
template_users = env.get_template('users.html')
template_user = env.get_template('user.html')
template_currencies = env.get_template("currencies.html")


def render_index(author, app):
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
        
def render_author(author):
    return template_author.render(
    		author_name=author.name,
    		group=author.group
		)


def render_users(users):
    return template_users.render(users=users)

def render_user(user, currencies):
    return template_user.render(
        user=user,
        currencies=currencies
    )


def render_currencies(currencies):
    return template_currencies.render(currencies=currencies)