class QueryBuilder():
    def __init__(self):
        self._matcher = All()

    def plays_in(self, team):
        self._matcher = And(self._matcher, PlaysIn(team))
        return self

    def has_at_least(self, value, attr):
        self._matcher = And(self._matcher, HasAtLeast(value, attr))
        return self

    def has_fewer_than(self, value, attr):
        self._matcher = And(self._matcher, HasFewerThan(value, attr))
        return self
    
    def one_of(self, query1, query2):
        self._matcher = Or(query1, query2)
        return self
    
    def build(self):
        return self._matcher

class And:
    def __init__(self, *matchers):
        self._matchers = matchers

    def test(self, player):
        for matcher in self._matchers:
            if not matcher.test(player):
                return False

        return True


class PlaysIn:
    def __init__(self, team):
        self._team = team

    def test(self, player):
        return player.team == self._team


class HasAtLeast:
    def __init__(self, value, attr):
        self._value = value
        self._attr = attr

    def test(self, player):
        player_value = getattr(player, self._attr)

        return player_value >= self._value

class All:
    def __init__(self, *matchers):
        self._matchers = matchers

    def test(self, player):
        return True
    
class Not:
    def __init__(self, *matchers):
        self._matchers = matchers
    def test(self, player):
        for m in self._matchers:
            if m.test(player):
                return False
            return True
        
class HasFewerThan:
    def __init__(self, value, attr):
        self._value = value
        self._attr = attr
    def test(self, player):
        player_value = getattr(player, self._attr)
        return player_value < self._value
    
class Or:
    def __init__(self, *matchers):
        self._matchers = matchers
    def test(self, player):
        for m in self._matchers:
            if m.test(player):
                return True
        return False