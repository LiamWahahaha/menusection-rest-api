from flask_restful import Resource, reqparse
from models.menusection import MenusectionModel


class Menusection(Resource):
    def get(self, id):
        menusection = MenusectionModel.find_by_id(id)

        if menusection:
            return {'MenuSection': [menusection.json()]}, 200
        else:
            return {'message': 'Menusection not found.'}, 204


    def post(self, id):
        parser = reqparse.RequestParser()
        parser.add_argument('name',
                            type=str,
                            required=True,
                            help='This field is required')
        data_payload = parser.parse_args()
        menusection = MenusectionModel.find_by_id(id)

        if menusection:
            if MenusectionModel.find_by_name(data_payload['name']):
                return {'message': 'The menusection \'{}\' already exists.'.format(data_payload['name'])}, 200
            else:
                menusection.name = data_payload['name']
                try:
                    menusection.save_to_db()
                except:
                    return {'message': 'An error has occurred modifying the menusection'}, 500
                return {'success': True, 'MenuSection': menusection.json()}, 201
        else:
            return {'message': 'No specific menusection can modify'}, 204


    def delete(self, id):
        menusection = MenusectionModel.find_by_id(id)

        if menusection:
            try:
                menusection.delete_from_db()
            except:
                return {'message': 'An error has occurred modifying the menusection'}, 500
            return {'success': True}, 200
        else:
            return {'message': 'Menusection not found.'}, 204


class MenusectionList(Resource):
    def get(self):
        return {'MenuSection': list(map(lambda x: x.json(), MenusectionModel.query.all()))}, 200


    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('name',
                            type=str,
                            required=True,
                            help='This field is required')
        data_payload = parser.parse_args()

        if MenusectionModel.find_by_name(data_payload['name']):
            return {'message': 'The menusection \'{}\' already exists.'.format(data_payload['name'])}, 200
        else:
            menusection = MenusectionModel(data_payload['name'])
            try:
                menusection.save_to_db()
            except:
                return {'message': 'An error has occurred inserting the menusection'}, 500
            return {'success': True, 'MenuSection': menusection.json()}, 201
