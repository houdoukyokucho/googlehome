# GoogleHome に任意の言葉を喋らせるプログラム

## 参考

- [Google Home を喋らせたい人のメモ](https://qiita.com/kiwsdiv/items/72d8a80c734e6d3e235b)
- [【SmartHome】Google Home Mini に Python を使って会話させるための基本](https://note.com/klayer123/n/nb8d8e5ca0ad4)

## 階層

階層は下の通りです。

```
.
├── googlehome.py
├── voice.txt
└── extra
    └── hoge.mp3
```

### googlehome.py

googlehome に喋らせるためのプログラムです。  
実行すると入力を求められます。入力出来るのは下記の 3 種類になります。

- 文字列
  - 入力された文字列を googlehome が喋ります。
- 空欄
  - voice.txt に記載されている文字列を googlehome が喋ります。
- ファイル名
  - extra/ 配下のファイル名を指定することで、その mp3 の内容を googlehome が喋ります。
