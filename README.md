# Moeda

Me and my girlfriend always argue who should walk down the apartment and get our pizza.
Our first choosing method was rock, paper, and scissors: whoever lost would bring the pizza. However, we thought about how this process can be unfair given the fact that our psychology interferes in the choosing process. The best way to determine who should pick up the pizza was the most random process possible to generate numbers.

As algorithms are pseudo-random, I found this website https://www.random.org/clients/http/ that generates random numbers based on atmospheric noise. This way, as the randomness is not in the algorithm but at the state of a physical system too complex for us to determine, it would be the closest possible for a true random number generator.

Nonetheless, I don't know the location where this atmospheric noise data is collected, there could be some tendencies. Think, for example, that the number is generated from the humidity at a desert. This system tends to have low humidity, therefore the numbers generated would tend to some value.

For this reason, I thought of the following system:
  - Through the RANDOM.ORG API I would generate an integer that would be 1 or 2;
  - I would keep track of how many times the code ran, so that I could assign the numbers (1 and 2) to the people (me and my girlfriend).
  - If the last time I was 1 and my girlfriend was 2, this time I would be 2 and she would be 1. Confusing? I just flipped the numbers!
  - Generate the number and the person whose number is assigned is doomed and should go get the pizza kkkkkkkkkkkkk.
  
We are open for new ideas for criticism for this method and new ideas of methods even more fair than this one.
