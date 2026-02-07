# Question: 6
# Transportation Mode Selection

def transport_mode() -> None:

    distance = int(input("Enter Distance: "))

    if distance < 3:
        mode = "Walk"
    elif distance < 16:
        mode = "Bike"
    else:
        mode = "Car"
    
    print(f"Take {mode}")

def app() -> None:
    transport_mode()

if __name__ == "__main__":
    app()