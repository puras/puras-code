import math
import random

import pygame as pg

width, height = 640, 480
# keys用来记录按键情况：WASD（依次对应）
keys = [False, False, False, False]
# hero_pos表示玩家位置
hero_pos = [100, 100]

# 跟踪玩家的精度变量，记录射出的箭头数和被击中的獾的数量
# 之后我们会用到这些信息用来计算射击精确度
acc = [0, 0]
# 跟踪箭头变量
arrows = []
# 定义一个定时器，使游戏里经过一段时间后就新建一个敌人
bad_timer = 100
bad_timer1 = 0
badguys = [[640, 100]]
health_val = 194

pg.init()
screen = pg.display.set_mode((width, height))

# 加载图片
hero_img = pg.image.load('resources/images/dude.png')
# 背景和风景
grass_img = pg.image.load('resources/images/grass.png')
castle_img = pg.image.load('resources/images/castle.png')
# 加载箭头
arrow_img = pg.image.load('resources/images/bullet.png')
# 加载獾
badguy_img1 = pg.image.load('resources/images/badguy.png')
badguy_img = badguy_img1

# 加载城堡健康值图片
healthbar_img = pg.image.load('resources/images/healthbar.png')
health_img = pg.image.load('resources/images/health.png')

# 加载胜利与失败 图片
gameover_img = pg.image.load('resources/images/gameover.png')
youwin_img = pg.image.load('resources/images/youwin.png')

# 加载声音文件并配置音量
hit = pg.mixer.Sound('resources/audio/explode.wav')
enemy = pg.mixer.Sound('resources/audio/enemy.wav')
shoot = pg.mixer.Sound('resources/audio/shoot.wav')
hit.set_volume(0.05)
enemy.set_volume(0.05)
shoot.set_volume(0.05)

# 加载游戏的背景音乐并让背景音乐一直不停的播放
pg.mixer.music.load('resources/audio/moonlight.wav')
pg.mixer.music.play(-1, 0.0)
pg.mixer.music.set_volume(0.25)

# 不停循环执行接下来的部分
# running变量会跟踪游戏是否结束
# exit_code变量会跟踪玩家是否胜利
running = True
exit_code = False

accuracy = 0

while running:
    # 在给屏幕画任何东西之前用黑色进行填充
    screen.fill(0)

    # 用图片填充背景，图片大小100*100
    for x in range(width // grass_img.get_width() + 1):
        for y in range(height // grass_img.get_height() + 1):
            screen.blit(grass_img, (x * 100, y * 100))
    # 画上背景
    screen.blit(castle_img, (0, 30))
    screen.blit(castle_img, (0, 135))
    screen.blit(castle_img, (0, 240))
    screen.blit(castle_img, (0, 345))

    # 首先获取鼠标与英雄的位置，然后获取通过Atan2函数得出的角度和弧度
    # 当英雄被旋转时，它的位置将会改变
    # 所以需要计算英雄的新位置，然后将其在屏幕上显示出来
    pos = pg.mouse.get_pos()
    angle = math.atan2(pos[1] - (hero_pos[1] + 32),
                       pos[0] - (hero_pos[0] + 26))
    hero_rot = pg.transform.rotate(hero_img, 360-angle*57.29)
    hero_pos1 = (hero_pos[0] - hero_rot.get_rect().width / 2,
                 hero_pos[1] - hero_rot.get_rect().height / 2)
    screen.blit(hero_rot, hero_pos1)

    # 在屏幕上画箭头
    # vely和velx的值是根据三角定理算出来的
    # 10是箭头的速度，if表过式是检查箭头是否超出来屏幕范围
    # 如果超出，就删除这个箭头
    # 第二个for表过式是循环来把箭头根据相应的旋转画出来
    for bullet in arrows:
        idx = 0
        velx = math.cos(bullet[0]) * 10
        vely = math.sin(bullet[0]) * 10
        bullet[1] += velx
        bullet[2] += vely
        if bullet[1] < -64 or bullet[1] > 640 or bullet[2] < -64 or bullet[2] > 480:
            arrows.pop(idx)

        idx += 1

        for projectile in arrows:
            a1 = pg.transform.rotate(arrow_img, 360 - projectile[0] * 57.29)
            screen.blit(a1, (projectile[1], projectile[2]))

    # 更新并显示坏蛋
    # 检查bad_timer是否为0，如果为0，创建一个獾，然后重新设置bad_timer
    # 第一个循环更新獾的X坐标，检查獾是否超出屏幕范围，如果超出，将獾删除
    # 第二个循环是来画出所有的獾
    if bad_timer == 0:
        badguys.append([640, random.randint(50, 430)])
        bad_timer = 100 - (bad_timer1 * 2)
        if bad_timer1 >= 35:
            bad_timer1 = 35
        else:
            bad_timer1 += 5
    index_badguy = 0
    for bad_guy in badguys:
        if bad_guy[0] < -64:
            badguys.pop(index_badguy)
        bad_guy[0] -= 1
        # 獾可以炸掉城堡
        # 如果獾的X坐标离左边小于64
        # 就删除獾，并减少游戏里的健康值，减少的大小为5到20里的随机数
        # 当然獾冲过来并且在碰到城堡时会消失
        bad_rect = pg.Rect(badguy_img.get_rect())
        bad_rect.top = bad_guy[1]
        bad_rect.left = bad_guy[0]
        if bad_rect.left < 64:
            hit.play()
            health_val -= random.randint(5, 20)
            badguys.pop(index_badguy)

        # 循环所有的坏蛋和所有的箭头来检查是否有碰撞
        # 如果碰撞上，删除獾，删除箭头，并且精准度的变量里面加1
        # 使用了PyGame内建功能来检查两个矩形是否交叉
        index_arrow = 0
        for bullet in arrows:
            bullet_rect = pg.Rect(arrow_img.get_rect())
            bullet_rect.left = bullet[1]
            bullet_rect.top = bullet[2]
            if bad_rect.colliderect(bullet_rect):
                enemy.play()
                acc[0] += 1
                badguys.pop(index_badguy)
                arrows.pop(index_arrow)
            index_arrow += 1
        index_badguy += 1
    for bad_guy in badguys:
        screen.blit(badguy_img, bad_guy)

    # 添加一个计时，使用PyGame默认的大小为24的字体来显示时间信息
    font = pg.font.Font(None, 24)
    survived_text = font.render(str((90000 - pg.time.get_ticks()) // 60000) + ':' + str((90000 - pg.time.get_ticks()) // 1000 % 60).zfill(2), True, (0, 0, 0))
    text_rect = survived_text.get_rect()
    text_rect.topright = [635, 5]
    screen.blit(survived_text, text_rect)

    # 画出城堡健康值
    # 首先画一个全红色的生命值条
    # 然后根据城堡的生命值往生命条里添加绿色
    screen.blit(healthbar_img, (5, 5))
    for health in range(health_val):
        screen.blit(health_img, (health + 8, 8))

    # 更新屏幕
    pg.display.flip()

    # 检查事件，如果有退出命令，则终止程序的执行
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            exit()
        # 根据按下的键来更新按键记录数组
        elif event.type == pg.KEYDOWN:
            if event.key == pg.K_w:
                keys[0] = True
            elif event.key == pg.K_a:
                keys[1] = True
            elif event.key == pg.K_s:
                keys[2] = True
            elif event.key == pg.K_d:
                keys[3] = True
        elif event.type == pg.KEYUP:
            if event.key == pg.K_w:
                keys[0] = False
            elif event.key == pg.K_a:
                keys[1] = False
            elif event.key == pg.K_s:
                keys[2] = False
            elif event.key == pg.K_d:
                keys[3] = False
        # 当玩家点击鼠标，就要射出一支箭
        # 这段代码会检查是否鼠标被点击了
        # 如果点击了就会得到鼠标的位置并根据玩家的和光标的位置计算出箭头旋转角度
        # 旋转角度的值存放在Arrows这个数组里
        if event.type == pg.MOUSEBUTTONDOWN:
            shoot.play()
            pos = pg.mouse.get_pos()
            acc[1] += 1
            arrows.append([math.atan2(pos[1] - (hero_pos1[1] + 32),
                                      pos[0] - (hero_pos1[0] + 26)),
                           hero_pos1[0] + 32, hero_pos1[1] + 26])

    if keys[0]:
        hero_pos[1] -= 5
    elif keys[2]:
        hero_pos[1] += 5
    if keys[1]:
        hero_pos[0] -= 5
    elif keys[3]:
        hero_pos[0] += 5
    bad_timer -= 1

    # 下面是一些胜利/失败的基本条件
    # 如果时间到了（90秒），停止运行游戏，设置游戏的输出
    # 如果城堡被毁，停止运行游戏，设置游戏的输出
    # 精确度是一直都需要计算的
    # 第一个IF表达式是检查是否时间到了
    # 第二个是检查城堡是否被摧毁了
    # 第三个是计算你的精准度
    # 之后，一个If表达式是检查你是赢了还是输出，然后显示相应的图片
    if pg.time.get_ticks() >= 90000:
        running = False
        exit_code = True
    if health_val <= 0:
        running = False
        exit_code = False
    if acc[1] != 0:
        accuracy = acc[0] * 1.0 / acc[1] * 100
        accuracy = ("%.2f" % accuracy)
    else:
        accuracy = 0

if not exit_code:
    pg.font.init()
    font = pg.font.Font(None, 24)
    text = font.render("Accuracy:" + str(accuracy) + "%", True, (255, 0, 0))
    text_rect = text.get_rect()
    text_rect.centerx = screen.get_rect().centerx
    text_rect.centery = screen.get_rect().centery + 24
    screen.blit(gameover_img, (0, 0))
    screen.blit(text, text_rect)
else:
    pg.font.init()
    font = pg.font.Font(None, 24)
    text = font.render("Accuracy:" + str(accuracy) + "%", True, (0, 255, 0))
    text_rect = text.get_rect()
    text_rect.centerx = screen.get_rect().centerx
    text_rect.centery = screen.get_rect().centery + 24
    screen.blit(youwin_img, (0, 0))
    screen.blit(text, text_rect)

while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            exit()
    pg.display.flip()