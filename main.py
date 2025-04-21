def main():
    with open('output.txt', 'w') as out_file:
        out_file.write(" ")

    try:
        with open('pokemon.txt', 'r') as file: # 'r' for read mode
            i = 1
            for line in file:
                out_string = "Pokemon 00"+str(i)+": " + line.strip()
                # print("Pokemon 00"+str(i)+": " + line.strip())
                i = i + 1

                with open('output.txt', 'a') as out_file:
                    out_file.write(out_string + "\n")

    except FileNotFoundError:
        print("File not found!")

    print("Thanks for using your pokedex formatter!")

if __name__ == "__main__":
    main()

# Some useful modes for file i/o
# 'r'  -- "read only"
# 'w'  -- "write (overwrite)"
# 'a'  -- "append"
# 'b'  -- "binary mode"
# '+'  -- "Read and write"