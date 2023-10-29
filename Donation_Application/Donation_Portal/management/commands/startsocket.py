from django.core.management.base import BaseCommand
import socket, time, threading, sys
sys.path.append('../C:\\Users\\Yashwardhan\\Desktop\\Major Project Soham\\Donation_Application\\Donation_Application\\Donation_Portal')
from Donation_Portal.models import Pool

HEADERSIZE = 10

class Command(BaseCommand):
    help = 'Open a socket in Django'
    # List to keep track of connected client sockets
    connected_clients = []
    def handle_client(self, client_socket):
        try:
            while True:
                data = client_socket.recv(1024)
                if not data:
                    break
                print(f"Received from {client_socket.getpeername()}: {data.decode()}")
        except Exception as e:
            print(f'Error: {e}')
        finally:
            client_socket.close()
            self.connected_clients.remove(client_socket)

    def send_periodic_messages(self):
        self.i = 0
        while 1:
            self.i+=1
            time.sleep(60)  # Send a message every 60 seconds
            self.msg = f'{self.i} The time is{time.time()}'
            pool = Pool.objects.all()
            obj = []
            for pl in pool:
                curr = []
                curr.append(pl.sender)
                curr.append(pl.receiver)
                curr.append(pl.sender_paypal_email)
                curr.append(pl.receiver_paypal_email)
                curr.append(pl.amount)
                # print(curr)
                obj.append(curr)                
                # print(tr.sender,tr.receiver,tr.sender_paypal_email,tr.receiver_paypal_email,tr.amount)
            # Emptying the pool
            Pool.objects.all().delete()            
            print(f"\n{self.i} The whole object is\n")
            print(str(obj)+'\n')
            self.msg = self.msg + "\n" + str(obj)
            self.msg = f"{len(self.msg):<{HEADERSIZE}}" + self.msg
            # self.msg += "[<User: soham>, 'NGO2', 'donor1@donor.com'"
            for client_socket in self.connected_clients:
                try:
                    client_socket.send(self.msg.encode())
                except Exception as e:
                    print(f'Error sending message to client: {e}')
    
    def handle(self, *args, **options):
        server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server_socket.bind(('127.0.0.10', 7777))
        server_socket.listen(5)
        print('Server is listening on port 7777')
        # Start the thread for sending periodic messages
        periodic_message_thread = threading.Thread(target=self.send_periodic_messages)
        periodic_message_thread.daemon = True
        periodic_message_thread.start()
        while True:
            client_socket, addr = server_socket.accept()
            print(f'Accepted connection from {addr}')
            # Add the client socket to the list of connected clients
            self.connected_clients.append(client_socket)
            # Start a thread to handle the client
            client_handler = threading.Thread(target=self.handle_client, args=(client_socket,))
            client_handler.start()