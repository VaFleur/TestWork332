import heapq

def find_top_transactions(transactions, n=3):
    return heapq.nlargest(n, transactions, key=lambda x: x["amount"])