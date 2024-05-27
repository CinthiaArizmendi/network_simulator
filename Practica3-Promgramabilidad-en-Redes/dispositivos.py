class Device:
    def __init__(self, ip_address):
        self.ip_address = ip_address
        self.connected_devices = []

    def connect(self, device):
        self.connected_devices.append(device)
        print(f"{self.ip_address} connected to {device.ip_address}")

    def send_message(self, device, message):
        if device in self.connected_devices:
            device.receive_message(message, self)
        else:
            print(f"{self.ip_address} cannot send message to {device.ip_address} - not connected")

    def receive_message(self, message, sender):
        print(f"{self.ip_address} received message from {sender.ip_address}: {message}")

class Router(Device):
    def __init__(self, ip_address):
        super().__init__(ip_address)
        self.routing_table = {}

    def add_route(self, destination_ip, next_hop):
        self.routing_table[destination_ip] = next_hop
        print(f"Route added: {destination_ip} -> {next_hop}")

    def route_message(self, destination_ip, message):
        if destination_ip in self.routing_table:
            next_hop = self.routing_table[destination_ip]
            self.send_message(next_hop, message)
        else:
            print(f"No route to {destination_ip}")
