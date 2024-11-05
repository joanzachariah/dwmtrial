from itertools import combinations

def get_input_data():
    num_transactions = int(input("Enter number of transactions: "))
    return [input(f"Enter items in transaction {i + 1} (separated by space): ").split() for i in range(num_transactions)]

def calculate_support(itemset, transactions):
    return sum(1 for transaction in transactions if set(itemset).issubset(transaction)) / len(transactions)

def generate_candidates(prev_freq_itemsets, length):
    return list(set(tuple(sorted(set(a) | set(b))) for a, b in combinations(prev_freq_itemsets, 2) if len(set(a) | set(b)) == length))

def apriori(transactions, min_support):
    items = sorted(set(item for transaction in transactions for item in transaction))
    freq_itemsets = set((item,) for item in items if calculate_support([item], transactions) >= min_support)
    
    all_freq_itemsets = freq_itemsets.copy()
    k = 2
    
    while freq_itemsets:
        candidates = generate_candidates(freq_itemsets, k)
        freq_itemsets = set(itemset for itemset in candidates if calculate_support(itemset, transactions) >= min_support)
        all_freq_itemsets.update(freq_itemsets)
        k += 1
    
    return sorted(all_freq_itemsets)

def generate_association_rules(freq_itemsets, transactions, min_confidence):
    rules = set()
    
    for itemset in freq_itemsets:
        for i in range(1, len(itemset)):
            antecedents = combinations(itemset, i)
            for antecedent in antecedents:
                consequent = tuple(set(itemset) - set(antecedent))
                antecedent_support = calculate_support(antecedent, transactions)
                rule_support = calculate_support(itemset, transactions)
                confidence = rule_support / antecedent_support if antecedent_support else 0
                if confidence >= min_confidence:
                    rules.add((tuple(sorted(antecedent)), tuple(sorted(consequent)), confidence))
    
    return list(rules)

if __name__ == "__main__":
    transactions = get_input_data()
    
    min_support = float(input("Enter minimum support (as a decimal): "))
    min_confidence = float(input("Enter minimum confidence (as a decimal): "))
    
    freq_itemsets = apriori(transactions, min_support)
    
    print("\nFrequent Itemsets:")
    for itemset in freq_itemsets:
        print(itemset)
    
    rules = generate_association_rules(freq_itemsets, transactions, min_confidence)
    
    print("\nAssociation Rules:")
    for antecedent, consequent, confidence in rules:
        print(f"Rule: {antecedent} -> {consequent} [Confidence: {confidence:.2f}]")