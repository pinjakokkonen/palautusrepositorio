from matchers import All, PlaysIn, HasAtLeast, HasFewerThan, And, Or

class QueryBuilder:
    def __init__(self, query=All()):
        self._query=query

    def plays_in(self, team):
        return QueryBuilder(PlaysIn(team))
    
    def has_at_least(self, value, attr):
        return QueryBuilder(And(self._query, HasAtLeast(value, attr)))
    
    def has_fewer_than(self, value, attr):
        return QueryBuilder(And(self._query, HasFewerThan(value, attr)))
    
    def one_of(self, one, two):
        return QueryBuilder(Or(one, two))

    def build(self):
        return self._query