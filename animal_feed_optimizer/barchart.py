import matplotlib.pyplot as plt

def plot_solution(result):
    ingredients = list(result.keys())
    values = list(result.values())

    plt.bar(ingredients, values)

    plt.title("Optimal Feed Composition")
    plt.xlabel("Ingredients")
    plt.ylabel("Quantity (kg)")

    cost_contribution = {
    k: results[k] * ingredients[k]["cost"]
    for k in ingredients
}

    plt.show()