import os
import time
import scripts.api as api
import scripts.commands as commands
import scripts.variables as variables


def timeStop(timing):
    time.sleep(timing - time.time() % timing)


def evolution(coin):
    try:
        data = {
            "symbol": api.get_symbol(coin),
            "price": api.get_price(coin, variables.currency)
        }

        print(f"= {data['symbol']} : ${data['price']}")

        while True:
            try:
                if data["price"] < api.get_price(coin, variables.currency):
                    data["price"] = api.get_price(coin, variables.currency)
                    print(f"{variables.Colors.GREEN}{chr(9650)} {data['symbol']} : ${data['price']}{variables.Colors.END}")

                elif data["price"] > api.get_price(coin, variables.currency):
                    data["price"] = api.get_price(coin, variables.currency)
                    print(f"{variables.Colors.RED}{chr(9660)} {data['symbol']} : ${data['price']}{variables.Colors.END}")

                timeStop(variables.reload_time)

            except KeyboardInterrupt:
                print("Interruption...")

                app()
                break

    except KeyError:
        print("Coin not found.")
        app()


def app():
    api.ping()

    while True:
        try:
            user_input = input("\n> ")
            break

        except (KeyboardInterrupt, EOFError) as e:
            exit()

    if user_input[0] == ".":
        commands.command(user_input)
        app()

    else:
        evolution(user_input.lower())


os.system("cls" if os.name == "nt" else "clear")
os.system("color" if os.name == "nt" else "")

print(variables.Texts.START)

app()