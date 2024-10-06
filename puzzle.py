from logic import *

# disclaimer! these are the four top 40 musicians when I googled it on Oct 6, 2024
# i only know a couple of them, and i am not explicitly endorsing
# any of their music or opinions
# <3 professor green


people = ["BillieEilish", "ChapelleRoan", "SabrinaCarpenter", "Shaboozey"]
homestates = ["Pennsylvania", "Virginia", "Missouri", "California"]

symbols = []

knowledge = And()

for person in people:
    for homestate in homestates:
        symbols.append(Symbol(f"{person}{homestate}"))

# Each person belongs to a homestate.
for person in people:
    knowledge.add(Or(
        Symbol(f"{person}Pennsylvania"),
        Symbol(f"{person}California"),
        Symbol(f"{person}Virginia"),
        Symbol(f"{person}Missouri")
    ))

# Only one homestate per person.
for person in people:
    for h1 in homestates:
        for h2 in homestates:
            if h1 != h2:
                knowledge.add(
                    Implication(Symbol(f"{person}{h1}"), Not(Symbol(f"{person}{h2}")))
                )

# Only one person per homestate.
for homestate in homestates:
    for p1 in people:
        for p2 in people:
            if p1 != p2:
                knowledge.add(
                    Implication(Symbol(f"{p1}{homestate}"), Not(Symbol(f"{p2}{homestate}")))
                    )
    

print(knowledge.formula())
