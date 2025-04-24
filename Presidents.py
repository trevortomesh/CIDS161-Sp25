def main():
    with open('presidents.txt', "r") as file:
        i = 1
        for line in file:
            print(str(i) + " " + line)
            out_string = str(i) + " " + line
            i = i + 1

            with open('numpresidents.txt', 'a') as out_file:
                out_file.write(out_string)




main()