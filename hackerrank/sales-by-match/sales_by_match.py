def sockMerchant(n, ar):
    colours_of_socks = {}
    num_of_pairs = 0
    
    for el in ar:
        if el in colours_of_socks:
            colours_of_socks[el] += 1
        else:
            colours_of_socks[el] = 1
    
    print (colours_of_socks)
    
    for colour in colours_of_socks:
        pairs = colours_of_socks[colour] // 2
        num_of_pairs += pairs
            
    return num_of_pairs
    # Write your code here

ar = [1,2,1,2,1,3,2]
test = sockMerchant(0, ar)