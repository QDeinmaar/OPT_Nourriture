from optimizer import optimize_feed

def main():
    results = optimize_feed()

    print("\n===== RESULTATS =====")
    print("Status :", results["status"])
    print(f"Maïs : {results['mais']} kg")
    print(f"Soja : {results['soja']} kg")
    print(f"Orge : {results['orge']} kg")
    print(f"Coût minimal : {results['cost']}")

if __name__ == "__main__":
    main()