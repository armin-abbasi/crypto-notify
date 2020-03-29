import json
import notify_module as notify
import helper_functions as _
from websocket import create_connection


max = int(input("Please enter your maximum price threshold: "))
min = int(input("Please enter your minimum price threshold: "))

CRYPTO_COMPARE_API_KEY = _.env('CRYPTO_COMPARE_API_KEY')

ws = create_connection(
    f"wss://streamer.cryptocompare.com/v2?api_key={CRYPTO_COMPARE_API_KEY}")

data = {
    "action": "SubAdd",
    "subs": ["24~CCCAGG~BTC~USD~m"]
}

print("Sending Data...")
ws.send(json.dumps(data))

print('Sent')
print("Receiving...")

while True:
    try:
        result = json.loads(ws.recv())

        proper_socket_type = result['TYPE'] == "24"
        check_price_range = 'LASTPRICE' in result.keys(
        ) and _.check_range(int(result['LASTPRICE']), min, max)

        if proper_socket_type and check_price_range:
            notify.pop("Crypto price exceeds your threshold",
                       f"Bitcoin latest price : {result['LASTPRICE']}")
    except:
        print('Error, connection terminated.')
        break

ws.close()
