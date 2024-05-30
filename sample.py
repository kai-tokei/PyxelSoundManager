import pyxel
from sound_manager import *

# サンプルコード
class App:
    def __init__(self):
        pyxel.init(160, 120, title="SoundManager Example")
        self.sound_manager = SoundManager()

        # サウンドの読み込み
        self.sound_manager.load_bgm("game-rock", "background")
        self.sound_manager.load_se("sample_se", "effect")

        pyxel.run(self.update, self.draw)

    def update(self):
        # BGMの再生
        self.sound_manager.play_bgm("background")

        # スペースキーが押されたら効果音を再生
        if pyxel.btnp(pyxel.KEY_SPACE):
            self.sound_manager.play_se("effect")

        # Qキーが押されたら全てのサウンドを停止
        if pyxel.btnp(pyxel.KEY_Q):
            self.sound_manager.stop()

    def draw(self):
        pyxel.cls(0)
        pyxel.text(10, 10, "Press SPACE for SE", pyxel.frame_count % 16)
        pyxel.text(10, 20, "Press Q to stop all sounds", pyxel.frame_count % 16)

# サンプルコードを実行
App()

