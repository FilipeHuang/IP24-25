def highest_items(menu):
    v_max = max(menu.values())
    return [j for j in menu if v_max == menu[j]]