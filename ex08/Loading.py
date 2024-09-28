from time import sleep



def ft_tdqm(lst: range) -> None:
    
    j = 1
    bar: str = "%|                           |"
    for i in range(lst):
        p = int((i / lst) * 100)
        if p > (3.7 * j):
            index = bar.find(" ") 
            bar = bar[:index] + "█" +bar[index + 1:]
            yield print(p, bar, i, "/", lst, end="\r") 
            j += 1
    print("100%|███████████████████████████| ", lst,"/", lst)