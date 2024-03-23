import matplotlib.pyplot as plt
import random

closing = False

def on_key_press(event):
    global mng, closing
    if event.key == 'escape':
        if closing:
            plt.close()
        else:
            closing = True
            mng.full_screen_toggle()

def show(values: list[int]):
    global mng
    indexs = list(range(len(values)))

    plt.plot(indexs, values, marker='o', linestyle='-')
    plt.xlabel("Temps")
    plt.ylabel("Nombre de dés partis par lancé")
    plt.title("Nombre de dés éliminés en fonction du lancé")

    plt.grid(True)
    plt.xticks(indexs[::2])
    plt.yticks(range(max(values) + 1))
    mng = plt.get_current_fig_manager()
    mng.full_screen_toggle()
    plt.connect('key_press_event', on_key_press)
    plt.show()

nbr_dice = 40
data = []
while nbr_dice != 0:
    current_eliminated = 0
    for i in range(nbr_dice):
        current_lance = random.randint(1, 6)
        if current_lance == 6:
            current_eliminated += 1
    nbr_dice -= current_eliminated
    data.append(current_eliminated)

show(data)