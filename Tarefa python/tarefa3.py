minha_lista_frutas = ["jaca", "melancia", "caqui", "banana", "mexerica"]


def sort(lst):
    if not lst:
        return []
    return (
        sort([x for x in lst[1:] if x < lst[0]])
        + [lst[0]]
        + sort([x for x in lst[1:] if x >= lst[0]])
    )


print(sort(minha_lista_frutas))