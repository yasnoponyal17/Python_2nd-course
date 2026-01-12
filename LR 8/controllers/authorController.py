class AuthorController:
    def __init__(self, jinja_env):
        self.env = jinja_env

    def render_index(self, app_info):
        return self.env.get_template("index.html").render(app=app_info)

    def render_author(self, app_info):
        return self.env.get_template("author.html").render(app=app_info)