from pulp import *
from data import ingredients, requirements

def optimize_feed():
    problem = LpProblem("Animal_feed_optimizer", LpMinimize)

    variables = {}

    for i in ingredients:
        variables[i] = LpVariable(i, lowBound=0)

    problem += lpSum(
        ingredients[i]["cost"] * variables[i]
        for i in ingredients
    )

    problem += lpSum(
        variables[i]
        for i in ingredients
    ) <= requirements["total_weight"]

    problem += lpSum(
        ingredients[i]["protein"] * variables[i]
        for i in ingredients
    ) >= requirements["min_protein"]

    problem += lpSum(
        ingredients[i]["energy"] * variables[i]
        for i in ingredients
    ) >= requirements["min_energy"]

    problem += variables["soja"] >= 5

    for i in ingredients:
        problem += variables[i] <= ingredients[i]["max_stock"]

    problem.solve()

    results = {}

    for i in ingredients:
        results[i] = value(variables[i])

    results["cost"] = value(problem.objective)
    results["status"] = LpStatus[problem.status]

    return results