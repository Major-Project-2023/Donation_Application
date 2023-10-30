from django.core.management.base import BaseCommand
import socket, time, threading, sys, pickle
sys.path.append('../C:\\Users\\Yashwardhan\\Desktop\\Major Project Soham\\Donation_Application\\Donation_Application\\Donation_Portal')
from Donation_Portal.models import Pool

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
                self.stdout.write(self.style.SUCCESS(f"Received from {client_socket.getpeername()}: {data.decode()}"))
        except Exception as e:
            self.stdout.write(self.style.WARNING(f'Error: {e}'))
        finally:
            client_socket.close()
            self.connected_clients.remove(client_socket)

    def send_periodic_messages(self):
        self.i = 0
        while 1:
            self.i+=1
            # Sleeping for 10s
            time.sleep(10)
            # Fetching from pool
            pool = Pool.objects.all()
            obj = []
            for pl in pool:
                curr = []
                curr.append(pl.sender_paypal_email)
                curr.append(pl.receiver_paypal_email)
                curr.append(pl.amount)
                obj.append(curr)                    
            # Emptying the pool
            Pool.objects.all().delete() 
            # Displaying the data object
            self.stdout.write(self.style.HTTP_INFO(f"\n{self.i} The whole object is\n"))
            self.stdout.write(self.style.HTTP_INFO(str(obj)+'\n'))
            # Pickeling the data object and sending it
            self.msg = obj
            self.msg_to_send = pickle.dumps(self.msg)
            for client_socket in self.connected_clients:
                try:
                    client_socket.send(self.msg_to_send)
                except Exception as e:
                    self.stdout.write(self.style.WARNING(f'Error sending message to client: {e}'))
    # Main function kinda
    def handle(self, *args, **options):
        server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server_socket.bind(('127.0.0.10', 7777))
        server_socket.listen(5)
        self.stdout.write(self.style.WARNING('Socket is listening on port 7777'))
        # Start the thread for sending periodic messages
        periodic_message_thread = threading.Thread(target=self.send_periodic_messages)
        periodic_message_thread.daemon = True
        periodic_message_thread.start()
        while True:
            client_socket, addr = server_socket.accept()
            self.stdout.write(self.style.WARNING(f'Accepted connection from {addr}'))
            # Add the client socket to the list of connected clients
            self.connected_clients.append(client_socket)
            # Start a thread to handle the client
            client_handler = threading.Thread(target=self.handle_client, args=(client_socket,))
            client_handler.start()