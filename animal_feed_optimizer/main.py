from optimizer import optimize_feed
from barchart import plot_solution
from data import ingredients

def main():
    results, variables = optimize_feed()

    print("\n===== RESULTATS =====")
    print("Status :", results["status"])
    print(f"Maïs : {results['mais']} kg")
    print(f"Soja : {results['soja']} kg")
    print(f"Orge : {results['orge']} kg")
    print(f"Coût minimal : {results['cost']}")

    result_plot = {
        i: variables[i].value()
        for i in variables
    }

    plot_solution(result_plot, ingredients)

if __name__ == "__main__":
    main()