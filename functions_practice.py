def hello():
    print("Hello user")

def pack(a, b, c):
    return [a, b, c]

def eat_lunch(food):
    if len(food) == 0:
        print("Lunchbox is empty")
    else:
        for i in range(len(food)):
            if i == 0:
                print(f"First I eat {food[0]}")
            else:
                print(f"Next I eat {food[i]}")


hello()
print(pack("a", "b", "c"))
eat_lunch([])
eat_lunch(["soup"])
eat_lunch(["chicken","spagetti","soup","salad"])
            