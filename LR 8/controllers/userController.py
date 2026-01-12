class UserController:
    def __init__(self, db_controller, jinja_env):
        self.db = db_controller
        self.env = jinja_env

    def render_users(self, app_info):
        users = self.db.conn.execute("SELECT * FROM user").fetchall()
        template = self.env.get_template("users.html")
        return template.render(users=users, app=app_info)

    def render_user_detail(self, user_id, app_info):
        user = self.db.conn.execute("SELECT * FROM user WHERE id = ?", (user_id,)).fetchone()
        if not user:
            return None
        subscriptions = self.db.get_user_subscriptions(user_id)
        template = self.env.get_template("user.html")
        return template.render(user=user, subscriptions=subscriptions, app=app_info)