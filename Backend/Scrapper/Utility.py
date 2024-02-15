

#ID Object
class ObjectID():

    def __init__(self, name, id):
        
        self.attributes = {
            'name':name,
            'id': id
        }
    def get(self, tag):
        try:
            return self.attributes[tag]
        except Exception as error:
            return False
    
    def set(self, tag, value):
        self.attributes[tag] = value
    
    def reset(self):
        self.attributes['name'] = None
        self.attributes['id'] = None

    def print(self):
        print("ObjectID Info:")
        print("name: ", self.attributes['name'])
        print("id: ", self.attributes['id'])



class State():

    def __init__(self):
        self.state = False
    
    def set_true(self):
        self.state = True

    def set_false(self):
        self.state = False
    
    def check(self):
        return self.state
