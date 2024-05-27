# main.py

from dispositivos import Device, Router
from utiles import create_network, simulate_communication

def main():
    router, device1, device2 = create_network()
    simulate_communication(router, device1, device2, "Hello, Device 2!")
    simulate_communication(router, device2, device1, "Hello, Device 1!")

if __name__ == "__main__":
    main()
