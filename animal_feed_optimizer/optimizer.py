from pulp import *
from data import ingredients, requirements

def optimize_feed():

    problem = LpProblem("Animal_Feed_Optimization", LpMinimize)

    x = {
        i: LpVariable(i, lowBound=0)
        for i in ingredients
    }

    for i in ingredients:
        problem += x[i] >= 1

        
    problem += lpSum(
        ingredients[i]["cost"] * x[i]
        for i in ingredients
    )

    problem += lpSum(x[i] for i in ingredients) == requirements["total_weight"]

    problem += lpSum(
        ingredients[i]["protein"] * x[i]
        for i in ingredients
    ) >= requirements["min_protein"]

    problem += lpSum(
        ingredients[i]["energy"] * x[i]
        for i in ingredients
    ) >= requirements["min_energy"]

    problem += lpSum(
        ingredients[i]["fiber"] * x[i]
        for i in ingredients
    ) <= requirements["max_fiber"]

    problem += lpSum(
        ingredients[i]["cost"] * x[i]
        for i in ingredients
    ) <= requirements["budget"]

    for i in ingredients:
        problem += x[i] <= ingredients[i]["max_stock"]

    problem.solve()

    results = {
    i: value(x[i]) for i in ingredients
}

    results["cost"] = value(problem.objective)
    results["status"] = LpStatus[problem.status]

    return results, x