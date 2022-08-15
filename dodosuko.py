'''
【問題】配列{"ドド","スコ"}からランダムに要素を標準出力し続け、『その並びが「ドドスコスコスコ」を3回繰り返したもの』に
一致したときに「ラブ注入♡」と標準出力して終了するプログラムを作成せよ(配点:5点)
'''

# 解答 コピー from # https://twitter.com/whosaysni/status/1554343676637491201?t=fsbHJmtZ5pobOmXegPcayA&s=09

if __name__ == '__main__':
    __import__('functools').reduce(
        lambda x, y: not ((print(f'ラブ注入♥') or exit(0)) if x[-12:]=='011101110111' else y)
        or print(f'{["ドド","スコ"][int(y)]}',end='')
        or x[-12:]+y,
        ('01'[b[0]%2] for b in iter(open('/dev/urandom', 'rb'))), ''
    )

'''
ポイント1: X or Y or Zの式において XがTrueならばXが返り、XがFalseならばY or Zが返り→YがTrueならば...
ポイント2: print('xxx') はxxxを標準出力に出してFalseを返す。(OS実行結果0が返るため)
ポイント3: reduceは初めにイテレーションの1つ目と2つ目をx,yとして受け取る。
'''