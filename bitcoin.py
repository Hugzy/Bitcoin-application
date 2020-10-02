import os

def help():
    return """
    supported commands are
    0 - exit
    ? - help
    1 - Check the balance
    2 - Create a new address
    3 - Send a coin to an address
    4 - List unspend transactions
    5 - Generate some coin
    """

def check_balance():
    # checks the balance of the bitcoin
    print("checking the balance...")
    return os.system("bitcoin-cli -regtest getbalance")

def create_address():
    # Creates a new address to send coins to
    print("creating new address...")
    return os.system("bitcoin-cli -regtest getnewaddress")

def send_coin():
    # Sends a coin to a specific address
    address = input("Please enter the address you want to send coins to ")
    amount = input("How much would you like to send to ")
    return os.system(f'bitcoin-cli -regtest sendtoaddress {address} {amount}')

def list_transactions():
    # List unspend transactions
    return os.system("bitcoin-cli -regtest listunspent 0")

def generate_coin():
    # Generate some coin
    address = input("please input the address you'd like to send generate coin to")
    return os.system("bitcoin-cli -regtest generatetoaddress 101 " + address)

def commands(command):
    return {
        '1': check_balance,
        '2': create_address,
        '3': send_coin,
        '4': list_transactions,
        '5': generate_coin,
    }.get(command, help)

if __name__ == "__main__":
    print(help())
    while True:
        command = input("Enter the command you'd like to run: ")
        if command == "exit" or command == '0':
            print("exiting application...")
            break
        print(commands(command)())