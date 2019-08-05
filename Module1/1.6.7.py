# n = int(input())
#
# classes = []
# questions = []
#
# for i in range(n):
#     cl_string = input()
#     classes.append(cl_string)
#
# q = int(input())
#
# for i in range(n):
#     q_string = input()
#     questions.append(q_string)

classes = ['A', 'B : A', 'C : A', 'D : B C']
questions = ['A B', 'B D', 'C D', 'D A']


classes = [  # список введённых строк
    'G : F',  # сначала отнаследуем от F, потом его объявим, корректный алгоритм все равно правильно обойдёт граф, независимо что было раньше: наследование или объявление
    'A',
    'B : A',
    'C : A',
    'D : B C',
    'E : D',
    'F : D',
    # а теперь другая ветка наследования
    'X',
    'Y : X A',  # свяжем две ветки наследования для проверки, обошла ли рекурсия предков Z и предков Y в поисках A
    'Z : X',
    'V : Z Y',
    'W : V',
]

questions = [  # список введённых запросов
    # 'A G',      # Yes   # A предок G через B/C, D, F
    # 'A Z',      # No    # Y потомок A, но не Y
    'A W',      # Yes   # A предок W через Y, V
    # 'X W',      # Yes   # X предок W через Y, V
    # 'X QWE',    # No    # нет такого класса QWE
    # 'A X',      # No    # классы есть, но они нет родства :)
    # 'X X',      # Yes   # родитель он же потомок
    # '1 1',      # No    # несуществующий класс
]


# def check_inheretion(child, parent):
#     for c in classes:
#         if len(c) > 1:
#             clfirst, clsecond = c.split(':')
#             if clfirst == child and parent in clsecond:
#                 return True
#             else:
#                 return check_inheretion(clfirst, parent)


def check_inheretion(parent, child):
    n=1
    for cl in classes:
        if child == parent:
            return True
        if len(cl) == 1:
            continue
        new_parent = cl.split(':')[0].strip()
        new_child = cl.split(':')[1].strip()
        if parent in new_child and child in new_parent:
            continue
        child_list = new_child.split()
        if new_parent in child or new_parent in parent:
            for ch in child_list:
                check_inheretion(ch, new_parent)

for i in questions:
    parent, child = i.split()
    if child == parent:
        print('Yes')
    elif check_inheretion(parent, child):
        print('Yes')
    else:
        print('No')

