from sample_madlibs import hp, code, zombie, hungergames
import random

if __name__ == "__main__":
    m = random.choice([hp, code, zombie, hungergames])
    m.madlib()

"""Time of Day: 5 in the evening
Body Part (plural): nose 
Color: blue
Verb (past tense): dead
Food: Burger
Noun: Love
Noun (plural): Socks
Adjective: Robust 
Adjective: Sexy
Adjective: Puny"""