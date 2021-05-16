# write your code here
# write your code here
sentance = []

for i in range(1000):
    a = input("- Choose a formatter: ")
    b = "plain bold italic header link inline-code ordered-list unordered-list new-line"
    c = b.split()
    if a == "!help":
        print("Available formatters: plain bold italic header link inline-code ordered-list unordered-list new-line")
        print("Special commands: !help !done")
    elif a == "!done":
        exit()
    elif a == "header":
        while True:
            d = int(input("- Level:"))
            e = input("- Text:")
            if 0 < d < 7:
                sd = "#" * d + " " + e
                sentance.append(sd)
                sentance.append("\n")
                print("".join(sentance))
                break
            else:
                print("The level should be within the range of 1 to 6")
    elif a == "new-line":
        sentance.append("\n")
        print("".join(sentance))
    elif a == "plain":
        sentance.append(input("- Text:"))
        print("".join(sentance))
    elif a == "link":
        f = input("- Label:")
        g = input("- URL:")
        sentance.append("[" + f + "]")
        sentance.append("(" + g + ")")
        print("".join(sentance))
    elif a == "bold":
        gj = "**" + input("- Text:") + "**"
        sentance.append(gj)
        print("".join(sentance))
    elif a == "italic":
        gj = "*" + input("- Text:") + "*"
        sentance.append(gj)
        print("".join(sentance))
    elif a == "inline-code":
        gj = "`" + input("- Text:") + "`"
        sentance.append(gj)
        print("".join(sentance))
    elif a == "ordered-list":
        while True:
            b = int(input("Number of rows:"))
            if b > 0:
                for i in range(1, b + 1):
                    c = input(f'Row #{i}: ')
                    sentance.append(f'{i}. {c}')
                    sentance.append("\n")
                break
            else:
                print("The number of rows should be greater than zero")
        print("".join(sentance))
    elif a == "unordered-list":
        while True:
            b = int(input("Number of rows:"))
            if b > 0:
                for i in range(1, b + 1):
                    c = input(f'Row #{i}: ')
                    sentance.append(f'* {c}')
                    sentance.append("\n")
                break
            else:
                print("The number of rows should be greater than zero")
        print("".join(sentance))

    else:
        print("Unknown formatting type or command. Please try again.")
