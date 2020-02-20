class Settings:
    def __init__(self):
        # 屏幕设置
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)

        # 飞船设置
        self.ship_speed = 1.5

        # 子弹设置
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        self.bullet_speed = 1
        self.bullet_limit = 3

        # 外星人设置
        self.alien_dir = 1
        self.alien_x_speed = 1
        self.alien_y_speed = 5