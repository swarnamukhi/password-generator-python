import random
def password_generator(pass_length,pool,chosen_set):
    pass_char= []
    for charset in chosen_set:
       pass_char.append(random.choice(charset))

    remaing_char = pass_length -len(pass_char)
    if remaing_char>0:
        pass_char.extend(random.choices(pool,k=remaing_char))
    random.shuffle(pass_char)
    return "".join(pass_char)  