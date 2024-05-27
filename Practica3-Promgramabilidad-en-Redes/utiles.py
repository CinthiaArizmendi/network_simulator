# utiles.py

from dispositivos import Device, Router

def create_network():
    router = Router("192.168.1.1")
    device1 = Device("192.168.1.2")
    device2 = Device("192.168.1.3")

    router.connect(device1)
    router.connect(device2)

    router.add_route("192.168.1.2", device1)
    router.add_route("192.168.1.3", device2)

    return router, device1, device2

def simulate_communication(router, sender, receiver, message):
    print(f"Simulating communication from {sender.ip_address} to {receiver.ip_address}")
    router.route_message(receiver.ip_address, message)
