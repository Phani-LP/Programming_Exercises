def counte(name1,  name2):
    name1_dict = {char:name1.count(char) for char in set(name1)}
    name2_dict = {char:name2.count(char) for char in set(name2)}
    total_count = sum(name1_dict.values()) + sum(name2_dict.values())
    common_count = 0
    for i in name1:
        if i in name2:
            common_count += min(name1_dict[i], name2_dict[i])
    remaining_count = total_count - 2*common_count
    return remaining_count

def result(remaining_count):
    flames =["Friends", "Love", "Affection", "Marriage", "Enemies", "Sibling"]
    index = (remaining_count % len(flames))-1
    return flames[index]

def main():
    name1 = input("Enter the first name: ").lower().replace(" ","")
    name2 = input("Enter the second name: ").lower().replace(" ","")
    rc = counte(name1,name2)
    res = result(rc)
    print(f"{name1} and {name2} are {res}")

if __name__ == "__main__":
    main()