from database import DataAccess, MongoDB


def save_review(json_data):
    data_access_obj = DataAccess()
    data_access_obj.mongodb_obj.add_review(json_data)
    return True


def get_review(self, query_filter={}):
    data_access_obj = DataAccess()
    return self.json_out(data_access_obj.mongodb_obj.get_review(query_filter=query_filter))
