from sqlalchemy import text

from models import User


def test_mocked_session_user_table(mocked_session):
    user_data = mocked_session.execute(text("SELECT * from user;")).all()
    assert user_data == [(1, 'Kevin'), (2, 'Dwight')]

def test_mocked_session_user_class(mocked_session):
    user = mocked_session.query(User).filter_by(id=2).first()
    assert user.name == "Dwight"
