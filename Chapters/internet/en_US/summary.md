# How the Internet Works: Summary

## What the chapter covers
Explains how a message finds one computer among billions:
- a hook about a video starting in under a second;
- a network of networks and routers;
- packets (a 3 MB photo is 2,055 packets), with TCP resending and reordering shown by a Python simulation (packets.py), and UDP for calls and games;
- IPv4 and its 4.3-billion limit, private addresses and NAT, IPv6, prefixes as ZIP codes, and Python's ipaddress module;
- ports and localhost:3000 (setting up web_apis);
- routing as shortest paths: a TikZ network of six routers, a worked next-hop example, and routing.py, which builds forwarding tables with Dijkstra and reroutes after a link fails;
- link-state (Dijkstra, OSPF) vs. distance-vector (Bellman-Ford, RIP), and BGP;
- the speed of light as a latency floor (New York to London, at least 56 ms round trip);
- DNS hierarchy, caching, and TTL;
- what happens when you load a page, including HTTPS (tied to RSA), and a TikZ diagram of the layers as nested envelopes.

## Key ideas
- Messages travel as numbered packets; TCP reorders and resends, UDP does not.
- IPv4 addresses are 32 bits (about 4.3 billion); prefixes group addresses into networks.
- Routers build forwarding tables (next hops) with shortest-path algorithms: Dijkstra in link-state routing, Bellman-Ford in distance-vector routing.
- DNS turns names into addresses through a cached hierarchy.
- Light in fiber sets a hard lower bound on delay.

## Changes in this pass
- New chapter, placed in volume 23 between graph_algorithms and web_apis, so the network comes before the HTTP that runs on top of it. Uses shortest_path (Dijkstra and Bellman-Ford, volume 22) and number_theory (RSA, volume 5). Volume 23 now has 7 chapters.
- Added pointers in web_apis (opening paragraph) and shortest_path (Bellman-Ford section).
- packets.py and routing.py were run, and their outputs are pasted in. Router D's table in the exercise was checked by running the code. All arithmetic (packet counts, 2^32, 2^128 per person, /16 and /8 sizes, NY–London and Denver–Tokyo distances by the haversine formula, light-speed round trips) was verified in Python.
- 8 exercises with answers (packet count, UDP for calls, prefix sizes, IPv6 per person, router D's table, Denver–Tokyo latency, the DNS TTL trade-off, and running traceroute).
- The pointer to Web APIs no longer says "the next chapter", since html now comes between them.
