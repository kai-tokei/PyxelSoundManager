import pyxel
import sys
import json

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
            if self._isExist(name, self.bgms):
                self.tick = 0
                self.isLoop = loop
                for ch, sound in enumerate(self.bgms[name]):
                    pyxel.sound(ch).set(*sound)
                    pyxel.play(ch, ch, loop=loop)
        else:
            self.tick = self._get_crt_tick()
            self._back_to_bgm()

    def play_se(self, name: str):
        """指定された名前のSEを再生する"""
        if self._isExist(name, self.ses):
            pyxel.play(self.seChannel, self.ses[name])
    
    def stop(self):
        pyxel.stop()

    def _back_to_bgm(self):
        """SE再生後にBGMに戻る"""
        if pyxel.play_pos(self.seChannel) is None:  # SEが鳴り終わったら
            pyxel.play(self.seChannel, [self.seChannel], self.tick, self.isLoop)  # 再びBGMを鳴らす

    def _get_crt_tick(self) -> int:
        """現在の再生位置を取得する"""
        for i in range(4):
            if pyxel.play_pos(i) is not None:
                self.tick = pyxel.play_pos(i)[1]
                return self.tick
        print("All channels are stopped!", file=sys.stderr)
        return -1

    def _isExist(self, name: str, sound_dict: dict) -> bool:
        """指定された名前の音声が存在するかチェックする"""
        if name not in sound_dict:
            print(f"Cannot find '{name}'", file=sys.stderr)
            return False
        return True
