import operator

def main():
    #This is a way to declare dictionaries
    dict = {
        "brand": "Ford",
        "model": "Mustang",
        "year": 1964
    }

    #Convert arr to dictionary
    arr = [10, 132, 324, 43, 0, 32]

    dict_arr = {}
    index = 0
    for el in arr:
        dict_arr[index] = el
        index += 1


    #Sorting technique 1
    test = {k: v for k, v in sorted(dict_arr.items(), key=lambda item: item[1])}
    #sorted_arr = sorted(dict_arr.items(), key=operator.itemgetter(0))
    
    #Sorting technique 2 does not work
    #dict(sorted(dict_arr.items(), key=lambda item: item[1]))

    print("Done")


if __name__ == "__main__":
    main()