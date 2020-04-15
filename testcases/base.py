from match_schema import match_schema
from match_schema import MatchSchemaException

def test1():
    schema = '''
    type: dict
    '''
    data = dict()

    exception = match_schema(schema = schema, data = data)
    assert exception is None

def test2():
    schema = '''
    type: dict
    '''

    data = list()
    exception = match_schema(schema = schema, data = data)

    assert isinstance(exception, MatchSchemaException)

def test3():
    schema = '''
    type: int
    '''

    data = 3
    exception = match_schema(schema = schema, data = data)
    assert exception is None

if __name__ == '__main__':
    test1()
    test2()
    test3()
