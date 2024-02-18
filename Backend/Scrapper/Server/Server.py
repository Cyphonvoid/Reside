import threading
#from Utility import *
#from Sockets import *
import time
import socket



class Status():

    def __init__(self, status):
        self.state = status

        if(isinstance(status, bool) == False):
            self.state = False

    def set_true(self):
        self.state = True

    def set_false(self):
        self.state = False

    def get(self):
        return self.state

class _id_setter():
    
    def __init__(self, object):
        self.object = object
    
    def name(self, val):
        self.object._name = val
    
    def id(self, val):
        self.object.identifier_token = val

    def expiry_date(self, data):
        self.object.expiration_date = data


class _id_getter():

    def __init__(self, object):
        self.object = object
        pass
    
    def name(self):
        return self.object._name
    
    def id(self):
        return self.object.identifier_token


class _ID():

    def __init__(self, id, name):
        self.identifier_token = id
        self._name = name
        self.expiration_date = None
        self.setter = _id_setter(object=self)
        self.getter = _id_getter(object=self)

    
    def attribute_category(self, cat):
        if(cat == 'getters'):
            return self.getter

        elif(cat == 'setters'):
            return self.setter
        
class ComponentID():
    
    def __init__(self, id, name):
        self.ComponentID = _ID(id, name)
    
    def read(self):
        return self.ComponentID.attribute_category('getters')
    
    def write(self):
        return self.ComponentID.attribute_category('setters')
    
class Atom():
    pass

class Molecule():
    pass

class Receptor():
    pass

#______________________________________


ERROR_CODE_SE = '--sender error--'
ERROR_CODE_RE = '--reciever error--'
SUCCESS_CODE_SE = '--sender active--'
SUCCESS_CODE_RE = '--reciever active--'
CLOSE_CONNECTION = '--Close Connection--'

class ERROR():

    SENDER = '--sender error--'
    RECIEVER = '--reciever error--'

class SUCCESS():
    SENDER = '--sender active--'
    RECIEVER = '--reciever active--'


class Message():

    def __init__(self, content, owner):
        self.content = content
        self.owner = owner
        if(owner == None):
            self.owner = "someone"

    def read(self):
        return (self.content, self.owner)
    
    def write(self, content):
        self.content = content

    def delete(self):
        self.content = None
        self.owner = None


class Storage():

    def __init__(self):
        self.outgoing = []
        self.incoming = []
    
    def get_handle(self):
        return self
    
    def push_to_outgoing(self, message):
        self.outgoing.append(Message(message, None))
    
    def push_to_incoming(self, message):
        self.incoming.append(Message(message, None))
    
    def pop_outgoing(self, num=-1):
        if(num == -1): return self.outgoing.pop()
        else:return self.outgoing.pop(num)
    
    def pop_incoming(self, num=-1):
        if(num == -1):return self.incoming.pop()
        else:return self.incoming.pop(num)
    
    def read_sent(self, at=-1):
        if(at == -1):return self.outgoing[-1]
        else:return self.outgoing[at]

    def read_recieved(self, at):
        if(at == -1):return self.incoming[-1]
        else:return self.incoming[at]


class Reciever():

    def __init__(self, socket, parent):
        self.socket = socket
        self.status = Status(True)
        self.reciever_thread = None
        self.reciever_thread = threading.Thread(target=self.thread)
        self.reciever_thread.setDaemon(True)
        self.reciever_status = Status(True)
        self.parent_component = parent
        self.socket_local_address = self.socket.getsockname()
        self.socket_remote_address = self.socket.getpeername()
        self.display_messages = True
     
    def display_incoming(self, val):
        self.display_messages = val

    def thread(self):
        #print(self.socket_remote_address, " reciever thread started")
        while(self.status.get() == True and self.reciever_status.get() == True):
            message = self.recieve()
            if(message == ERROR.RECIEVER):
                #print("thread error caught", message)
                return
            self.parent_component.storage.push_to_incoming(message)


    def recieve(self):
        #Need to detech the offline socket state on other side or when it closes it in general 
        if(self.status.get() == False): 
            return ERROR.RECIEVER
        
        Message = None
        try:
            message = self.socket.recv(1024).decode('utf-8')

            if(message == None or message == CLOSE_CONNECTION):
                self.status.set_false()
                self.parent_component.status.set_false()
                return ERROR.RECIEVER
            if(self.display_messages == True): print("Recieved From:",str(self.socket_remote_address) + ">", message)
            return message
        except Exception as error:
            return ERROR.RECIEVER
            
        return message

   

    def activate(self):
        self.status.set_true()
        self.reciever_status.set_true()
        self.reciever_thread.start()
    
    def deactivate(self):
        self.status.set_false()
        self.reciever_status.set_false()

    def shutdown(self):
        self.status.set_false()
        self.reciever_status.set_false()
        self.socket = None
        self.parent_component = None
    
    def reboot(self, socket, parent):
        self.status.set_true()
        self.reciever_status.set_true()
        self.socket = socket
        self.parent_component = parent


class Sender():

    def __init__(self, socket, parent):
        self.socket = socket
        self.status = Status(True)
        self.parent_component = parent
        self.display_message = True
        self.socket_local_address = self.socket.getsockname()
        self.socket_remote_address = self.socket.getpeername()
    
    def display_outgoing(self, val):
        self.display_message = val

    def __check_ready__(self):
        if(self.socket == None):
            self.status.set_false()
        else:
            self.status.set_true()

    def send(self, message):
        if(self.status.get() == False):
            return ERROR.SENDER
        
        try:
            self.socket.send(message.encode('utf-8'))
            if(self.display_message == True):print("Sent To:" + str(self.socket_remote_address) + ">", message)
            return SUCCESS.SENDER
        except Exception as error:
            print("Error in Sender Object", error)
            self.parent_component.status.set_false()
            return ERROR.SENDER
    
    
    def activate(self):
        #print("in sencer activate")
        self.status.set_true()
        self.__check_ready__()

    def deactivate(self):
        self.status.set_false()

    def shutdown(self):
        self.status.set_false()
        self.socket = None
        self.parent_component = None
    
    def reboot(self, socket, parent):
        self.status.set_true()
        self.socket = socket
        self.parent_component = parent

    
class ClientHandle():
    #Client socket object which needs the a socket to be oassed in as constructor
    def __init__(self, socket):
        self.socket = socket
        self._local_address = socket.getsockname()
        self._remote_address = socket.getpeername()
        self.status = Status(True)
        self.storage = Storage()
        self.sender = Sender(socket, self)
        self.reciever = Reciever(socket, self)
        self._display_messages = True
        self.callback = None

        
    def attach_callback(self, callback):
        self.callback = callback

    def send_message(self, message):
        if(self.status.get() == False):
            self.callback(self)
            return ERROR.SENDER
        
        success = self.sender.send(message)

        if(success == ERROR.SENDER):
            self.callback(self)
            self.status.set_false()
        
        return SUCCESS.SENDER

    def storage(self):
        return self.storage
    
    def recieve_message(self):
        if(self.status.get() == False):
            self.callback(self)
            return ERROR.RECIEVER
        
        #self.recieve_event_callback(self)
        value = self.storage.read_recieved()
        return value


    def print(self):
        print("Socket Information:", " Remote: ", self.remote_address())
        pass

    def local_address(self):
        return self._local_address
    
    def remote_address(self):
        return self._remote_address

    def shutdown(self):
        self.sender.shutdown()
        self.reciever.shutdown()
       
    def reboot(self):
        self.sender.reboot(self.socket, self)
        self.reciever.reboot(self.socket, self)

    def open(self):
        #print("in handle open()")
        self.status.set_true()
        self.reciever.activate()
        self.sender.activate()
        
    def close(self):
        self.status.set_false()
        self.sender.shutdown()
        self.reciever.shutdown()
        self.socket.close()
    
    def display_messages(self, val):
        self._display_messages = val

        if(val == True):
            self.sender.display_outgoing(True)
            self.reciever.display_incoming(True)
        else:
            self.sender.display_outgoing(False)
            self.sender.display_outgoing(False)


    def state(self):
        return self.status.get()

#Listener Sockets will listen to incoming calls and produce client sockets
class Listener():

    def __init__(self):
        self.listener_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self._local_address = None
        self.client_socket = []
        self.limit = None
        self.listening_thread = None
        self.status = Status(False)
        self.connection_state = Status(False)
        self.callback = None
        self.callback_arg = None

    def __produce_sockets__(self):

        try:
            self.listener_socket.listen()
            client_socket, address = self.listener_socket.accept()
            new_socket = ClientHandle(client_socket)
            new_socket.open()
            if(self.callback != None): self.callback(new_socket)
            self.client_socket.append(new_socket)
        except Exception as error:
            pass
      
    def __listen__(self):
        if(self.status.get() == False):
            return
        
        if(self.limit != None):
            for i in range(0, self.limit+1):
               if(self.status.get() == False or self.connection_state.get() == False):
                   return
               self.__produce_sockets__()

        elif(self.limit == None):
            while True:
               if(self.status.get() == False or self.connection_state.get() == False):
                   return
               self.__produce_sockets__()

    def set_limit(self, num):
        self.limit = num

    def host_with(self, IP, PORT):
        try:
            self.listener_socket.bind((IP, PORT))
            self.connection_state.set_true()
            self._local_address = self.listener_socket.getsockname()
            print("Listerned socket successfully connected...")
        except Exception as error:
            self.connection_state.set_false()
            print("[Error hosting]:", error)
            raise error

    def __run__(self):
        self.listening_thread = threading.Thread(target=self.__listen__)
        self.listening_thread.start()

    def attach_event_handler(self, callback):
        self.callback = callback

    def local_address(self):
        return self._local_address
    
    def open(self):
        if(self.connection_state.get() == False):
            self.status.set_false()
        elif(self.connection_state.get() == True): 
            self.status.set_true()
            print("Listener socket is open and ready.....")
            self.__run__()
       
    def close(self):
        self.status.set_false()
        self.connection_state.set_false()
        self.listener_socket.close()

#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
CLOSE_CONNECTION = '--Close Connection--'

class Input():

    def __init__(self, status):
        self.state = Status(status)

    def user_input(self):
        if(self.state.get() == True):
            return input()
        elif(self.state.get() == False):
            return None

    def open(self):
        self.state.set_true()

    def close(self):
        self.state.set_false()


class MultiClientServer():

    def __init__(self):
        self.clients = []
        self.client_listener = Listener()
        self.client_listener.attach_event_handler(self.push_new_client)
        self.client_listener.set_limit(10)
        self.current_client = None
        self.status = Status(False)
        self.input = Input(True)
        self.reciever_thread = threading.Thread(target=self.__thread__, daemon=True)
        self.send_all_flag = False
        self._message = None
    
    def push_new_client(self, client):
        self.clients.append(client)
        client.attach_callback(self.server_callback)
        print(client.remote_address(), " Connected...")
    
    def server_callback(self, client):
        address = client.remote_address()
        self.filter_clients(client)
        print(str(address) + " got disconnected....")
        self.current_client = None

    def __thread__(self):
        #This thread needs to be synchronized with the main thread when deleting stuff like current client
        while self.status.get() == True:
            value = self.recieve_message()
            if(value == ERROR.RECIEVER):
                self.filter_clients(self.current_client)
                self.current_client = None
            
            if(self.current_client == None):
                time.sleep(1)
                
            
    def select_client(self, num):
        try:
            num = int(num)
            if(num > len(self.clients)-1 or num < 0):
                return
            self.current_client = self.clients[num]
        except Exception as error:
            pass

    def close_client(self):
        self.current_client.close()

        counter = 0; 
        for client in self.clients:
            if(client == self.current_client):
                self.clients.pop(counter)
            
            counter+=1

    def display(self):
        print("         MultiClientServer")
        print("____________________________________")
        print("Hosted On:", self.client_listener.local_address())  

        
    def send_message(self, message):
        if(len(self.clients) == 0):
            print("[No Clients Available]")
            return None
        
        if(self.current_client == None):
            print("[Current client is None and not selected..]")
            return None
        
        if(message == 'exit'):
            self.input.close()
            self.close()
            return None
        try:
            if(self.current_client.state() == True):
                success = self.current_client.send_message(message)
                if(success == ERROR.SENDER):
                    print("[Error recieved in send:", ERROR.SENDER)
                    return False
                #print(self.current_client.remote_address(), "> sent:", message)
                return True
            else:
                return False
        except Exception as error:
            print("[Error recieved in send:", error)
            return False
        

    def recieve_message(self):
        if(len(self.clients) == 0):
            print("[No Clients Available")
            return None
        
        if(self.current_client == None):
            print("[Current client is None and not selected..]")
            return None
        
        message = None
        try:
            if(self.current_client.state() == True):
                message = self.current_client.recieve_messae()
                if(message == ERROR.RECIEVER):
                    print("[Error recieved]:", ERROR.RECIEVER)
                    return False
                print(self.current_client.remote_address(),"> recieved:", message)
                return message
            else:
                return False
        except Exception as error:
            print("[Error recieved]:", error)
            return False
    
    def __clients(self):

        #Display clients
        counter = 0; 
        for client in self.clients:
            print("client [" + str(counter) + "]")
            client.print()
            counter += 1
        
        print("Select >>", end="")
        val = input()
        self.select_client(val)

    def __disconnect_client(self, num):

        #Display clients
        counter = 0; 
        for client in self.clients:
            print("client [" + str(counter) + "]")
            client.print()
            counter += 1
        
        print("Select to disconnect >>", end="")
        val = input()
        temp = ""
        for i in range(0, len(self.clients)):
            if(i == int(val)):
                temp = self.clients.pop(i)
                break
        
        print("client dropped", temp.remote_address())


    def load_messages(self, message):
        self._message = message
        pass

    def run(self, IP, PORT):
        self.status.set_true()
        self.input.open()
        self.client_listener.host_with(IP, PORT)
        self.client_listener.open()
        self.display()
        #self.reciever_thread.start()
        
        while True:
            val = input()

            if(val == '-exit'):
                print("_______________Closed__________________")
                self.send_close_header()
                self.close_all_clients()
                self.close()
                break

            if(val == '-select'):
                self.send_all_flag = False
                self.__clients()
                continue
            elif(val == 'close'):
                self.__disconnect_client()
                pass
            if(val == '-select all'):
                self.send_all_flag = True
    
            success = None
            if(val == 'send load'):
                self.send_message(self._message)

            if(self.send_all_flag == False):
                success = self.send_message(val)
            else: 
                for client in self.clients:
                    success = client.send_message(val)
            if(success == ERROR.SENDER):
                self.filter_clients(self.current_client)
                self.current_client = None


    def filter_clients(self, _client):
        counter = 0
        for client in self.clients:
            if(client == _client):
                self.clients.pop(counter)
            counter += 1

        pass
    def send_close_header(self):
        for client in self.clients:
            client.send_message(CLOSE_CONNECTION)

    def close_all_clients(self):
        for client in self.clients:
            client.close()
        
    def close(self):
        self.client_listener.close()
        self.input.close()
    


server = MultiClientServer()
server.run('192.168.1.222', 9999)
server.close()
