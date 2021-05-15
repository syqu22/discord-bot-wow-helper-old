def test_get_log_info(logs):
    assert logs.get_log_info()

def test_get_title(logs):
    assert logs.get_title()

# RETURNS EMPTY LIST WHEN FROM PTR
def test_get_characters(logs):
    assert logs.get_characters()

def test_get_fights(logs):
    assert logs.get_fights()

def test_get_log_duration(logs):
    assert logs.get_log_duration()

def test_get_zone(logs):
    assert logs.get_zone()

def test_get_game_version(logs):
    assert logs.get_game_version()

#TODO add comments, improve them a bit and add rest
