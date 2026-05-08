import matplotlib.pyplot as plt

def plot_solution(result, ingredients):

    names = list(ingredients.keys())
    values = [result[i] for i in names]

    plt.figure()
    plt.bar(names, values)

    plt.title("Optimal Feed Composition")
    plt.xlabel("Ingredients")
    plt.ylabel("Quantity (kg)")

    plt.show()

    cost = [result[i] * ingredients[i]["cost"] for i in names]

    plt.figure()
    plt.bar(names, cost)

    plt.title("Cost Contribution per Ingredient")
    plt.xlabel("Ingredients")
    plt.ylabel("Cost")

    plt.show()