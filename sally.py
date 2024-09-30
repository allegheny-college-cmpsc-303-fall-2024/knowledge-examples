""" Glimpse into propositional logic """

from logic import *

rain = Symbol("rain") # It is raining
school = Symbol("school") # Sally went to class
minecraft = Symbol("minecraft") # Sally played Minecraft

""" Knowledge to Represent
1. If it's not raining, then Sally went to class
2. Sally either went to class or played Minecraft
3. Sally cannot go to class and play Minecraft at the same time
4. Sally went to class
Query: Is it raining or not?
"""
knowledge = And(
    Implication(Not(rain), school),
    Or(school, minecraft),
    Not(And(school, minecraft)),
    school
)

print(knowledge.formula())
print(model_check(knowledge, rain))
