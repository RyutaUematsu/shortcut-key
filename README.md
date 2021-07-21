# shortcut-key
## 概要
キーボードのカスタムショートカットを簡単に作成できるかつ自由度が無限のアプリ
Ryuta Uematsu 専用
## 外部サービス
GCP Speach to Text
Nature Remo API

## ショートカットキー 設定
 {
        'operation': ショートカット名,
        'hot-keys': ショートカットキー（同時押し）, 
        'function': 発火する関数
 },


src/settings.py
```
SHOURTCUTS = [
    # エアコンをつける
    {
        'operation': "Aircon on",
        'hot-keys': ['CTRL', 'A', 'UP'],   # 必ずキーは3つで設定する
        'function': 'aircon_on'
    },
    # エアコンを消す
    {
        'operation': "Aircon off",
        'hot-keys': ['CTRL', 'A', 'DOWN'],
        'function': 'aircon_off'
    },
    # 部屋の電気をつける
    {
        'operation': "Light on",
        'hot-keys': ['CTRL', 'SHIFT', 'L'],
        'function': 'room_light_power'
    },
    # マイクからの音声をタイプ入力する
    {
        'operation': "Light on",
        'hot-keys': ['CTRL', 'ALT', 'SPACE'],
        'function': 'input_from_mic',
    }
]
```
