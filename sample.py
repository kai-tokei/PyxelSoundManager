import pyxel
from sound_manager import SoundManager

class App:
    def __init__(self):
        pyxel.init(160, 120, title="Sound Manager Example")
        self.sound_manager = SoundManager()
        
        # BGMとSEの読み込み
        self.sound_manager.load_bgm('sample_bgm', 'bgm1')
        self.sound_manager.load_se('sample_se', 'se1')
        
        # BGMを再生
        self.sound_manager.play_bgm('bgm1')

        pyxel.run(self.update, self.draw)

    def update(self):
        # スペースキーが押されたらSEを再生
        if pyxel.btnp(pyxel.KEY_SPACE):
            self.sound_manager.play_se('se1')

    def draw(self):
        pyxel.cls(0)
        pyxel.text(38, 60, "Press SPACE to play SE", 7)

App()
