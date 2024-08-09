head_cnt = int(input())
foot_cnt = int(input())

ok_cnt = 0

for i in range(head_cnt + 1):
    head_chicken = i
    head_rabbit = head_cnt - head_chicken
    if head_rabbit * 4 + head_chicken * 2 == foot_cnt:
        print('Chicken=' + str(head_chicken) + ' Rabbit=' + str(head_rabbit))
        ok_cnt += 1

if ok_cnt == 0:
    print('No solution!')