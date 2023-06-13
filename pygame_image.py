import sys
import pygame as pg


def main():
    pg.display.set_caption("はばたけ！こうかとん")
    screen = pg.display.set_mode((800, 600))
    clock  = pg.time.Clock()
    bg_ing = pg.image.load("ex01/fig/pg_bg.jpg")
    kk_ing = pg.image.load("ex01/fig/3.png")
    kk_ing = pg.transform.flip(kk_ing,True,False)
    kk_ing2 = pg.transform.rotozoom(kk_ing,10,1.0)
    kk_ing_l = [kk_ing,kk_ing2]
    bg_x = 0  # Initial x-coordinate for the background image
    tmr = 0
    flap_tmr = 0
    flap_interval = 10  # 羽ばたく間隔を調整
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT: 
                return
            
        

        screen.blit(bg_img, [0, 0])
        screen.blit(bg_img, (bg_x, 0))  # Display the background image at the updated x-coordinate
        screen.blit(kk_ing,[300,200])  # Display the character image
        pg.display.update()
         # Alternate the display of kk_ing based on the time step
        if tmr % 20 < 10:  # Display kk_ing for 10 time steps, then hide for the next 10 time steps
            screen.blit(kk_ing)
        
        pg.display.update()
        bg_x -= 1
        if bg_x <= -800:
            bg_x = 0  # Reset the x-coordinate when the image moves completely off the screen  
            
        # Update the counter x
        #x = (x + 1) % 1600
         
        tmr += 1        
        clock.tick(60)
        
        


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()