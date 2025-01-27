import math
from collections import Counter

# https://en.wikipedia.org/wiki/Entropy_(information_theory)
# https://cocomelonc.github.io/malware/2022/11/05/malware-analysis-6.html
# https://rendazhang.medium.com/information-theory-series-1-entropy-and-shannon-entropy-a20a2101108e

def shannon_entropy(data):
    # freq de elemntos
    freq = Counter(data)
    total = len(data)
    
    # calculo entropia de shannon -> H(X) = -Σ p(x) log2 p(x)
    entropy = 0
    for count in freq.values():
        prob = count / total
        entropy -= prob * math.log2(prob)
    
    return entropy

# exemplo
data = ['a', 'b', 'a', 'c', 'a', 'b', 'b']
print(f"Shannon Entropy: {shannon_entropy(data):.4f}")

