print("Hello ", end="")
print("World!")

num = 0
print(f"Num {num}")
print(f"Num ", num, sep="&&")

print("Bem-Vindo")
print("[1] Nome")
print("[2] IBan")
opt = input("-> ")

match opt:
    case 1:
        print("Nome")
    case 2:
        print("IBan")
    case default:
        print("Deves achar")