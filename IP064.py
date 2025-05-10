def rename(menu, old_name, new_name):
    if old_name in menu:
        menu[new_name] = menu.pop(old_name)
    return menu