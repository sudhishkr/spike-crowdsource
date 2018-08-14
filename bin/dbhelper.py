from database import DataAccess, MongoDB


def save_review_2_db(json_data):
    data_access_obj = DataAccess()
    data_access_obj.mongodb_obj.add_review(json_data)
    return True


def read_review_4m_db():
    return
