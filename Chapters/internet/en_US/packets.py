import random

random.seed(4)
message = "Meet me at the library at 3:30, after band practice."
size = 8   # characters per packet

# Sender: chop the message into numbered packets
packets = []
for start in range(0, len(message), size):
    packets.append((start // size, message[start:start + size]))
print("Sending", len(packets), "packets")

# Receiver: keep the packets that arrive, keyed by number
received = {}
needed = list(range(len(packets)))
round_number = 1

while needed:
    in_flight = [packets[n] for n in needed]
    random.shuffle(in_flight)                  # packets take different routes
    arrived = []
    for number, data in in_flight:
        if random.random() < 0.25:             # 1 packet in 4 gets lost
            continue
        received[number] = data
        arrived.append(number)
    needed = [n for n in range(len(packets)) if n not in received]
    print("Round", round_number, "arrived:", arrived, "still missing:", needed)
    round_number += 1

# Put the packets back in order
print("".join(received[n] for n in range(len(packets))))
