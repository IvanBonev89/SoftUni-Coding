def to_do_note(note):
    to_do_note = []
    while True:
        note = input()
        if note == "End":
            break
        else:
            to_do_note.append(note)

    sorted_list = sorted(to_do_note, key = lambda x: int(x.split("-")[0]))
    new_list = list(note.split("-")[1] for note in sorted_list)
    return new_list

a = ''
print(to_do_note(a))
