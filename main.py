import pyxel
import json
import sys

MUSIC_FILE = "game-rock"
SE_SOUND_INDEX = 0  # 効果音のサウンドインデックス
seChannel = 0

class SoundManager:
    def __init__(self):
        self.bgms = {}  # BGMを格納する辞書
        self.ses = {}  # SEを格納する辞書
        self.seStack = 63  # 使用可能なサウンドバンクの数
        self.tick = None  # 現在の再生位置
        self.se = ""  # 現在再生中のSE名
        self.bgm = ""  # 現在再生中のBGM名
        self.isLoop = True  # BGMがループ再生するかどうか
        self.seChannel = 3  # SEが再生されるチャンネル

    def load_bgm(self, path: str, name: str):
        """指定されたパスからBGMを読み込み、辞書に格納する"""
        try:
            with open(f"./sounds/{path}.json", "rt") as fin:
                self.bgms[name] = json.loads(fin.read())
        except FileNotFoundError:
            print(f"Error: File '{path}.json' not found", file=sys.stderr)

    def load_se(self, path: str, name: str):
        """指定されたパスからSEを読み込み、サウンドバンクにセットする"""
        if self.seStack > 3:
            try:
                with open(f"./sounds/{path}.json", "rt") as fin:
                    self.ses[name] = json.loads(fin.read())
                for ch, sound in enumerate(self.ses[name]):
                    if ch == 0:
                        pyxel.sound(self.seStack).set(*sound)
                self.seStack -= 1
            except FileNotFoundError:
                print(f"Error: File '{path}.json' not found", file=sys.stderr)
        else:
            print("Error: Sound Bank is overflow!!", file=sys.stderr)

    def play_bgm(self, name: str, loop: bool = True):
        """指定された名前のBGMを再生する"""
        if self.tick is None:
            if self.isExist(name, self.bgms):
                self.tick = 0
                self.isLoop = loop
                for ch, sound in enumerate(self.bgms[name]):
                    pyxel.sound(ch).set(*sound)
                    pyxel.play(ch, ch, loop=loop)
        else:
            self.tick = self.get_crt_tick()
            self.back_to_bgm()

    def play_se(self, name: str):
        """指定された名前のSEを再生する"""
        if self.isExist(name, self.ses):
            pyxel.play(self.seChannel, self.ses[name])

    def back_to_bgm(self):
        """SE再生後にBGMに戻る"""
        if pyxel.play_pos(self.seChannel) is None:  # SEが鳴り終わったら
            pyxel.play(self.seChannel, [self.seChannel], self.tick, self.isLoop)  # 再びBGMを鳴らす

    def get_crt_tick(self) -> int:
        """現在の再生位置を取得する"""
        for i in range(4):
            if pyxel.play_pos(i) is not None:
                self.tick = pyxel.play_pos(i)[1]
                return self.tick
        print("All channels are stopped!", file=sys.stderr)
        return -1

    def isExist(self, name: str, sound_dict: dict) -> bool:
        """指定された名前の音声が存在するかチェックする"""
        if name not in sound_dict:
            print(f"Cannot find '{name}'", file=sys.stderr)
            return False
        return True


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

