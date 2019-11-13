from ttt.networking.ttt_client import TTTClient


def main():
    client = TTTClient()
    client.start()
    client.play()

if __name__ == '__main__':
    main()