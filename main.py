import pyxel
import json

MUSIC_FILE = "game-rock"
SE_SOUND_INDEX = 0  # 効果音のサウンドインデックス
seChannel = 0

class App:
    def __init__(self):
        pyxel.init(160, 120, title="Pyxel Tracker Player")
        pyxel.load("sepack.pyxres") # SE読み込み用
        with open(f"./musics/{MUSIC_FILE}.json", "rt") as fin:
            self.music = json.loads(fin.read())

        self.bg_ticks = None  # BGMの経過tick数を管理
        pyxel.run(self.update, self.draw)

    def update(self):
        pressed = pyxel.btnp(pyxel.KEY_SPACE)
        if self.bg_ticks is None:
            if pressed:
                for ch, sound in enumerate(self.music):
                    pyxel.sound(ch).set(*sound)
                    pyxel.play(ch, ch, loop=True)
                    self.bg_ticks = 0
        else:
            if pressed: # ２回目以降スペースを押すとSEを鳴らす
                print("se")
                pyxel.play(seChannel, [20]) # 38はSEの番号
                self.se = seChannel
            self.bg_ticks = pyxel.play_pos(1)[1] # 現在の再生位置
            if pyxel.play_pos(seChannel) is None: # SEが鳴り終わったら
                pyxel.play(seChannel, [seChannel], self.bg_ticks, True) # 再びBGMを鳴らす
        pyxel.cls(0)
        pyxel.text(20, 40, "Press [SPACE] to play/stop BGM.", 7)
        pyxel.text(20, 64, "Press [ESC] to exit.", 7)

    def draw(self):
        pass

App()

