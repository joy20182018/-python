from Queue_other import QueueData


def hotPotato(namelist, number):
    q = QueueData()
    for name in namelist:
        q.enqueue(name)

    while q.size() > 1:
        for i in range(number):
            q.enqueue(q.dequeue())

        # q.dequeue()

        print(q.dequeue(), end= ' ')

    print("")

    if q.isEmpty():
        print("error")
    else:
        return q.dequeue()


name = ['wang', 'xiao', 'ming', 'hong', 'xie',  'ewsdfw']
number = 4
print("最后一个人")
print(hotPotato(name, number))