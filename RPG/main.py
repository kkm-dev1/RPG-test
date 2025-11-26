import arcade

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
PLAYER_SPEED = 5

class RPG(arcade.Window):
    def __init__(self):
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, "RPG 초기 형태")
        arcade.set_background_color((144, 238, 144))  # 연두색
        
        # 초기화 - setup() 호출 전에 접근될 수 있는 속성들을 초기화
        self.player = None
        self.player_list = None
        # keys_pressed는 이벤트 핸들러에서 사용되므로 __init__에서 초기화 필요
        self.keys_pressed = set()

    def setup(self):
        """게임 리소스 초기화"""
        # SpriteSolidColor의 생성자: width, height, center_x, center_y, color
        # 색상은 RGBA255 형식이므로 키워드 인자로 명시적으로 전달
        # 또는 arcade.color.BLUE 같은 색상 상수 사용 가능
        self.player = arcade.SpriteSolidColor(32, 32, color=(0, 0, 255, 255))

        # SpriteList
        self.player_list = arcade.SpriteList()
        self.player_list.append(self.player)

        # 플레이어 초기 위치 설정
        self.player.center_x = SCREEN_WIDTH // 2
        self.player.center_y = SCREEN_HEIGHT // 2
        
        # 속도 속성 초기화 (on_update에서 사용되므로 필수)
        self.player.change_x = 0
        self.player.change_y = 0

    def on_draw(self):
        """화면 그리기"""
        # 최신 arcade 버전에서는 clear()를 사용
        self.clear()
        # player_list가 None일 수 있으므로 체크
        if self.player_list:
            self.player_list.draw()

    def on_update(self, delta_time):
        """게임 로직 업데이트"""
        # player가 초기화되지 않았을 경우 처리
        if self.player is None:
            return
            
        # 현재 눌려있는 키에 따라 속도 설정
        # 여러 키를 동시에 누를 수 있도록 개선
        self.player.change_x = 0
        self.player.change_y = 0
        
        if arcade.key.LEFT in self.keys_pressed:
            self.player.change_x = -PLAYER_SPEED
        if arcade.key.RIGHT in self.keys_pressed:
            self.player.change_x = PLAYER_SPEED
        if arcade.key.DOWN in self.keys_pressed:
            self.player.change_y = -PLAYER_SPEED
        if arcade.key.UP in self.keys_pressed:
            self.player.change_y = PLAYER_SPEED
        
        # 플레이어 이동
        self.player.center_x += self.player.change_x
        self.player.center_y += self.player.change_y
        
        # 화면 경계 체크 - 플레이어가 화면 밖으로 나가지 않도록 제한
        # 좌우 경계 체크
        if self.player.left < 0:
            self.player.left = 0
        elif self.player.right > SCREEN_WIDTH:
            self.player.right = SCREEN_WIDTH
        
        # 상하 경계 체크
        if self.player.bottom < 0:
            self.player.bottom = 0
        elif self.player.top > SCREEN_HEIGHT:
            self.player.top = SCREEN_HEIGHT

    def on_key_press(self, key, modifiers):
        """키를 누를 때 호출되는 메서드"""
        # 눌려있는 키를 집합에 추가
        if key in (arcade.key.UP, arcade.key.DOWN, arcade.key.LEFT, arcade.key.RIGHT):
            self.keys_pressed.add(key)

    def on_key_release(self, key, modifiers):
        """키를 놓을 때 호출되는 메서드"""
        # 놓은 키를 집합에서 제거
        if key in self.keys_pressed:
            self.keys_pressed.discard(key)


async def main():
    """pygbag을 위한 async main 함수"""
    game = RPG()
    game.setup()
    arcade.run()

if __name__ == "__main__":
    # pygbag을 사용할 때는 asyncio.run()을 사용
    import asyncio
    asyncio.run(main())
