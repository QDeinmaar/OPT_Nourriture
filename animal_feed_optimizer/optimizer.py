from pulp import *
from data import ingredients, requirements

def optimize_feed():
    problem = LpProblem("Animal_feed_optimizer", LpMinimize)

    variables = {}

    for i in ingredients:
        variables[i] = LpVariable(i, lowBound=0)

    # Objective: minimize cost
    problem += lpSum(
        ingredients[i]["cost"] * variables[i]
        for i in ingredients
    )

    # Total weight constraint
    problem += lpSum(
        variables[i]
        for i in ingredients
    ) <= requirements["total_weight"]

    # Protein constraint (IMPORTANT FIX: >=)
    problem += lpSum(
        ingredients[i]["protein"] * variables[i]
        for i in ingredients
    ) >= requirements["min_protein"]

    # Stock constraints
    for i in ingredients:
        problem += variables[i] <= ingredients[i]["max_stock"]

    # Solve ONCE
    problem.solve()

    # Results
    results = {}

    for i in ingredients:
        results[i] = value(variables[i])

    results["cost"] = value(problem.objective)
    results["status"] = LpStatus[problem.status]

    return results