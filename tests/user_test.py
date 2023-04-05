def test_get_user_from_email(user):
    res = user.get_by_email('student1@fylebe.com')
    assert res.username == 'student1'
    assert res.id == 1

def test_get_user_from_id(user):
    res = user.get_by_id(1)
    assert res.username == 'student1'
    assert res.email == 'student1@fylebe.com'

def test_get_user_not_present_id(user):
    res = user.get_by_id(1000)
    assert res == None

def test_get_user_not_present_email(user):
    res = user.get_by_email('notPresent@flyebe.com')
    assert res == None
