from abc import ABC, abstractmethod


class SQLQuery:
    def __init__(self):
        self.select = ""
        self.from_table = ""
        self.joins = []
        self.where = []
        self.order_by = ""

    def show(self):
        query = f"SELECT {self.select} FROM {self.from_table}"

        if self.joins:
            query += " " + " ".join(self.joins)

        if self.where:
            query += " WHERE " + " AND ".join(self.where)

        if self.order_by:
            query += f" ORDER BY {self.order_by}"

        print(query)
        print('\n')


class QueryBuilder(ABC):

    @abstractmethod
    def select(self):
        pass

    @abstractmethod
    def from_table(self):
        pass

    @abstractmethod
    def where(self):
        pass

    @abstractmethod
    def join(self):
        pass

    @abstractmethod
    def order_by(self):
        pass

    @property
    @abstractmethod
    def query(self):
        pass


class UserQueryBuilder(QueryBuilder):

    def __init__(self):
        self.reset()

    def reset(self):
        self._query = SQLQuery()

    @property
    def query(self):
        q = self._query
        self.reset()
        return q

    def select(self):
        self._query.select = "id, name, email"

    def from_table(self):
        self._query.from_table = "users"

    def where(self):
        self._query.where.append("active = 1")

    def join(self):
        self._query.joins.append(
            "LEFT JOIN orders ON users.id = orders.user_id"
        )

    def order_by(self):
        self._query.order_by = "name ASC"


class ProductQueryBuilder(QueryBuilder):

    def __init__(self):
        self.reset()

    def reset(self):
        self._query = SQLQuery()

    @property
    def query(self):
        q = self._query
        self.reset()
        return q

    def select(self):
        self._query.select = "id, name, price"

    def from_table(self):
        self._query.from_table = "products"

    def where(self):
        self._query.where.append("price > 100")

    def join(self):
        pass  # нет join

    def order_by(self):
        self._query.order_by = "price DESC"


class Director:

    def __init__(self):
        self.builder = None

    def set_builder(self, builder):
        self.builder = builder

    def build_simple_query(self):
        self.builder.select()
        self.builder.from_table()

    def build_full_query(self):
        self.builder.select()
        self.builder.from_table()
        self.builder.join()
        self.builder.where()
        self.builder.order_by()


if __name__ == "__main__":
    director = Director()

    print("Query for users")
    builder = UserQueryBuilder()
    director.set_builder(builder)
    director.build_full_query()
    query = builder.query
    query.show()

    print("Query for products")
    builder = ProductQueryBuilder()
    director.set_builder(builder)
    director.build_full_query()
    query = builder.query
    query.show()

    print("Custom query")
    builder.select()
    builder.from_table()
    builder.where()
    query = builder.query
    query.show()