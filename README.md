# SoundManager Class for Pyxel

This `SoundManager` class is designed to manage background music (BGM) and sound effects (SE) in a Pyxel game. It allows loading, playing, and stopping sounds, with support for interrupting BGMs with SEs. The class is intended to work with JSON files created using the PyxelTracker music creation software.

## Features

- Load BGM and SE from JSON files.
- Play and stop BGM and SE.
- Manage sound channels and sound bank allocation.
- Support for looping BGMs.
- Handle SE interruptions and resume BGMs afterwards.

## Installation

Ensure you have the following installed:

- Python 3.x
- Pyxel
- JSON files created using PyxelTracker

To install Pyxel, run:
```bash
pip install pyxel
```

## Usage

### Initial Setup

First, import the necessary modules and create an instance of the `SoundManager` class:

```python
import pyxel
from sound_manager import SoundManager

sound_manager = SoundManager()
```

### Loading Sounds

Load BGM and SE from JSON files. The files should be located in the `./sounds/` directory.

```python
sound_manager.load_bgm('path_to_bgm_file', 'bgm_name')
sound_manager.load_se('path_to_se_file', 'se_name')
```

### Playing Sounds

Play a BGM with optional looping (default is `True`):

```python
sound_manager.play_bgm('bgm_name', loop=True)
```

Play an SE:

```python
sound_manager.play_se('se_name')
```

### Stopping Sounds

Stop all sounds:

```python
sound_manager.stop()
```

### Managing SE Channel

Set the channel for SE playback (default is `2`):

```python
sound_manager.set_seChannel(1)
```

### Example

Here is a complete example of using the `SoundManager` class in a Pyxel game:

```python
import pyxel
from sound_manager import SoundManager

class App:
    def __init__(self):
        pyxel.init(160, 120, caption="Sound Manager Example")
        self.sound_manager = SoundManager()
        self.sound_manager.load_bgm('example_bgm', 'bgm1')
        self.sound_manager.load_se('example_se', 'se1')
        self.sound_manager.play_bgm('bgm1')

        pyxel.run(self.update, self.draw)

    def update(self):
        if pyxel.btnp(pyxel.KEY_SPACE):
            self.sound_manager.play_se('se1')

    def draw(self):
        pyxel.cls(0)
        pyxel.text(50, 60, "Press SPACE to play SE", pyxel.frame_count % 16)

App()
```

## Methods

### `set_seChannel(ch: int)`

Set the channel for SE playback.

- `ch`: The channel number to set for SE playback.

### `load_bgm(path: str, name: str)`

Load a BGM from a JSON file.

- `path`: The path to the BGM JSON file (relative to `./sounds/`).
- `name`: The name to associate with the loaded BGM.

### `load_se(path: str, name: str)`

Load an SE from a JSON file and allocate it to a sound bank.

- `path`: The path to the SE JSON file (relative to `./sounds/`).
- `name`: The name to associate with the loaded SE.

### `play_bgm(name: str, loop: bool = True)`

Play a BGM.

- `name`: The name of the BGM to play.
- `loop`: Whether to loop the BGM (default is `True`).

### `play_se(name: str)`

Play an SE.

- `name`: The name of the SE to play.

### `stop()`

Stop all sounds.

### `_back_to_bgm()`

Resume the BGM after an SE has finished playing. This method is called internally.

### `_get_crt_tick() -> int`

Get the current playback position. This method is called internally.

### `_isExist(name: str, sound_dict: dict) -> bool`

Check if a sound with the specified name exists in the given dictionary. This method is called internally.

- `name`: The name of the sound to check.
- `sound_dict`: The dictionary to check in (either `self.bgms` or `self.ses`).

## Error Handling

- Raises `FileNotFoundError` if the specified JSON file is not found.
- Raises `OverflowError` if the sound bank is full and cannot load more SEs.
- Raises `KeyError` if trying to play a sound that has not been loaded.
- Raises `RuntimeError` if all channels are stopped unexpectedly.

## License

This project is licensed under the MIT License. See the LICENSE file for more details.

# Pyxel用 SoundManager クラス

この`SoundManager`クラスは、Pyxelゲームでの背景音楽（BGM）と効果音（SE）を管理するためのものです。サウンドの読み込み、再生、停止を行い、SEによるBGMの割り込みもサポートしています。このクラスは、PyxelTracker音楽制作ソフトを用いて作成されたJSONファイルと互換性があります。

## 特徴

- JSONファイルからBGMとSEを読み込む
- BGMとSEの再生と停止
- サウンドチャンネルとサウンドバンクの管理
- ループ再生のサポート
- SE割り込み後にBGMを再開

## インストール

以下の環境が必要です：

- Python 3.x
- Pyxel
- PyxelTrackerで作成されたJSONファイル

Pyxelをインストールするには、以下のコマンドを実行してください：

```bash
pip install pyxel
```

## 使用方法

### 初期設定

まず、必要なモジュールをインポートし、`SoundManager`クラスのインスタンスを作成します：

```python
import pyxel
from sound_manager import SoundManager

sound_manager = SoundManager()
```

### サウンドの読み込み

JSONファイルからBGMとSEを読み込みます。ファイルは`./sounds/`ディレクトリに配置します。

```python
sound_manager.load_bgm('path_to_bgm_file', 'bgm_name')
sound_manager.load_se('path_to_se_file', 'se_name')
```

### サウンドの再生

BGMを再生します（ループ再生はデフォルトで`True`）：

```python
sound_manager.play_bgm('bgm_name', loop=True)
```

SEを再生します：

```python
sound_manager.play_se('se_name')
```

### サウンドの停止

全てのサウンドを停止します：

```python
sound_manager.stop()
```

### SEチャンネルの管理

SE再生用のチャンネルを設定します（デフォルトは`2`）：

```python
sound_manager.set_seChannel(1)
```

### 使用例

以下は、Pyxelゲームで`SoundManager`クラスを使用する完全な例です：

```python
import pyxel
from sound_manager import SoundManager

class App:
    def __init__(self):
        pyxel.init(160, 120, caption="Sound Manager Example")
        self.sound_manager = SoundManager()
        self.sound_manager.load_bgm('example_bgm', 'bgm1')
        self.sound_manager.load_se('example_se', 'se1')
        self.sound_manager.play_bgm('bgm1')

        pyxel.run(self.update, self.draw)

    def update(self):
        if pyxel.btnp(pyxel.KEY_SPACE):
            self.sound_manager.play_se('se1')

    def draw(self):
        pyxel.cls(0)
        pyxel.text(50, 60, "Press SPACE to play SE", pyxel.frame_count % 16)

App()
```

## メソッド

### `set_seChannel(ch: int)`

SE再生用のチャンネルを設定します。

- `ch`: SE再生用のチャンネル番号

### `load_bgm(path: str, name: str)`

JSONファイルからBGMを読み込みます。

- `path`: BGM JSONファイルのパス（`./sounds/`からの相対パス）
- `name`: 読み込んだBGMに対応する名前

### `load_se(path: str, name: str)`

JSONファイルからSEを読み込み、サウンドバンクに割り当てます。

- `path`: SE JSONファイルのパス（`./sounds/`からの相対パス）
- `name`: 読み込んだSEに対応する名前

### `play_bgm(name: str, loop: bool = True)`

BGMを再生します。

- `name`: 再生するBGMの名前
- `loop`: BGMをループ再生するかどうか（デフォルトは`True`）

### `play_se(name: str)`

SEを再生します。

- `name`: 再生するSEの名前

### `stop()`

全てのサウンドを停止します。

### `_back_to_bgm()`

SE再生後にBGMを再開します。このメソッドは内部で呼び出されます。

### `_get_crt_tick() -> int`

現在の再生位置を取得します。このメソッドは内部で呼び出されます。

### `_isExist(name: str, sound_dict: dict) -> bool`

指定された名前のサウンドが指定された辞書に存在するかをチェックします。このメソッドは内部で呼び出されます。

- `name`: チェックするサウンドの名前
- `sound_dict`: チェック対象の辞書（`self.bgms`または`self.ses`）

## エラーハンドリング

- 指定されたJSONファイルが見つからない場合、`FileNotFoundError`を発生させます。
- サウンドバンクがいっぱいでSEを読み込めない場合、`OverflowError`を発生させます。
- 読み込まれていないサウンドを再生しようとした場合、`KeyError`を発生させます。
- 全てのチャンネルが予期せず停止した場合、`RuntimeError`を発生させます。

## ライセンス

このプロジェクトはMITライセンスの下でライセンスされています。詳細はLICENSEファイルを参照してください。


