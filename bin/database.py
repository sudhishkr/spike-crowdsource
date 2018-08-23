import pymongo
import ast
import json
from bson import json_util
from bson.objectid import ObjectId


class DataAccess(object):

    def __init__(self):
        mongodb_url = "mongodb://heroku_h5t46r8p:hba6f3a68mco0j9cbst7ps6cjo@ds121282.mlab.com:21282/heroku_h5t46r8p"
        self.mongodb_obj = MongoDB(url=mongodb_url)


class MongoDB(object):

    def __init__(self, url):
        self.client = pymongo.MongoClient(url)
        self.default_db = self.client.get_default_database()
        self.collection_review = self.default_db["review"]

    @staticmethod
    def json_out(results):
        json_results = []
        for result in results:
            json_results = result
        return ast.literal_eval(json.dumps(json_results, default=json_util.default))

    ####################
    # COMMENT
    ####################

    def add_review(self, review_data):
        self.collection_review.insert(review_data)
        return True

    def get_review(self, query_filter={}):
        return self.json_out(self.collection_review.find(query_filter))

    def delete_review(self, query_filter={}):
        query_data = self.get_review(query_filter=query_filter)
        if len(query_data) == 1:
            self.collection_review.remove(ObjectId(query_data[0]["_id"]["$oid"]))
            return True
        else:
            return False
