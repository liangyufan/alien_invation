class Settings:
    def __init__(self):
        # 屏幕设置
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)

        # 飞船设置
        self.ship_lives = 2

        # 子弹设置
        self.bullet_width = 300
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        self.bullet_limit = 3

        # 加快游戏节奏因子
        self.speedup_scale = 1.1
        self.score_scale = 1.5

        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        self.ship_speed = 1.5
        self.bullet_speed = 1
        # 外星人设置
        self.alien_dir = 1
        self.alien_x_speed = 1
        self.alien_y_speed = 10
        self.alien_point = 10

    def increase_speed(self):
        self.ship_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.alien_x_speed *= self.speedup_scale
        self.alien_y_speed *= self.speedup_scale
        self.alien_point = int(self.alien_point * self.score_scale)