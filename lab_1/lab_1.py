globalList = [
    {"name": "Bob", "phone": "0631234567", "age": "19", "group": "КБ-251"},
    {"name": "Emma", "phone": "0631234567", "age": "20", "group": "КБ-251"},
    {"name": "Jon",  "phone": "0631234567", "age": "19", "group": "КБ-251"},
    {"name": "Zak",  "phone": "0631234567", "age": "18", "group": "КБ-251"}
]

def printAllList(listForPrinting):
    for item in listForPrinting:
        print(f"Name = {item['name']} | Phone = {item['phone']} | Age = {item['age']} | Group = {item['group']}")

def findPosition(listForFinding, nameForFinding):
    index = 0
    for item in listForFinding:
        if item["name"] < nameForFinding: 
            index += 1
        else:
            break
    return index

def addElemToSortedList(listForAdd, newElem):
    positionForInsert = findPosition(listForAdd, newElem["name"])
    listForAdd.insert(positionForInsert, newElem)
    return

def getElement():
    name = input("Please enter the name: ")
    phone = input("Please enter the phone: ")
    age = input("Please enter the age: ")
    group = input("Please enter the group: ")
    return {"name": name, "phone": phone, "age": age, "group": group}

def deleteElem(listForDel, name):
    indexForDel = findPosition(listForDel, name)
    if indexForDel < len(listForDel) and listForDel[indexForDel]["name"] == name:
        del listForDel[indexForDel]
        return True
    else:
        return False

def updateElement(listForUpdate, name):
    indexForUpdate = findPosition(listForUpdate, name)
    if indexForUpdate < len(listForUpdate) and listForUpdate[indexForUpdate]["name"] == name:
        print("Student found! New info: ")
        newElem = getElement()

        deleteElem(listForUpdate, name)
        addElemToSortedList(listForUpdate, newElem)
        return True
    else:
        return False

def main():
    while True:
        chouse = input("Please enter the commanfd [C - add new elem, D - delete elem,  P - print all List, U - update element, X - exit] ")
        match chouse:
            case "C" | "c" :
                newElem = getElement()
                addElemToSortedList(globalList, newElem)
            case "D" | "d":
                nameElemForDel = input("Please enter the name for delete ")
                if deleteElem(globalList, nameElemForDel):
                    print("Element has been deleed")
                else:
                    print("Element hasn't been found")
            case "P" | "p" :
                printAllList(globalList)
            case "U" | "u" :
                nameElemForUpdate = input("Please enter the name to update: ")
                if updateElement(globalList, nameElemForUpdate):
                    print("Element was updeted")
                else:
                    print("Element wasn't found")
            case "X" | "x" :
                print("Exit")
                break
            case _:
                print("Wrong operation")


main()