from sys import exit

def gold_room():
    print "This room is full of gold. HOw much do you take?"

    next = raw_input("> ")
    if next.isdigit():
        how_much = int(next)
    else:
        dead("Man, learn to type a number.")

    if how_much < 50:
        print "Nice, you're not greedy, you win!"
        exit(0)
    else:
        dead("You greedy bastard!")

def dead(why):
    print why, "Good job!"
    exit(0)


# gold_room()

wait = raw_input("type somethign ")

if wait == "hello":
    print "yep you typed it"
