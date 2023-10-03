import random
import sys
import pygame as pg


WIDTH, HEIGHT = 1600, 900


def main():
    pg.display.set_caption("逃げろ！こうかとん")
    screen = pg.display.set_mode((WIDTH, HEIGHT))
    bg_img = pg.image.load("ex02/fig/pg_bg.jpg")
    kk_img = pg.image.load("ex02/fig/3.png")
    kk_img = pg.transform.rotozoom(kk_img, 0, 2.0)
    clock = pg.time.Clock()
    
    bomb = pg.Surface((10, 10))
    pg.draw.circle(bomb, (255, 0, 0), (10, 10), 10)
    bomb_rtc = bomb.get_rect()
    x,y = random.randint(0,WIDTH),random.randint(0,HEIGHT) #ランダムな座標を設定する。
    bomb_rtc.center = (x,y)#練習問題１
    vx, vy = +5, +5 #練習２　爆弾の移動
     
    tmr = 0
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT: 
                return

        screen.blit(bg_img, [0, 0])
        screen.blit(kk_img, [900, 400])
        bomb_rtc.move_ip(vx,vy) #練習問題２：爆弾を移動させる
        screen.blit(bomb, bomb_rtc)#表示と座標の設定
        pg.display.update()
        tmr += 1
        clock.tick(60)


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()