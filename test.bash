#!/bin/bash
# SPDX-FileCopyrightText: 2026 CHAI YI SHAN
# SPDX-License-Identifier: BSD-3-Clause

ng () {                          # 関数ngの定義
        echo ${1}行目のテスト失敗   # $1はngの1番目の引数
        res=1                    # 追加: 失敗したことを記録
}

res=0

out=$(seq 5 | ./plus)                  # 表の1行目: plusの出力を変数outに記録
[ "$?" = 0 ]      || ng "$LINENO"
[ "${out}" = 15 ] || ng "$LINENO"

### STRANGE INPUT ###
out=$(echo あ | ./plus)           #計算できない値を入力してみる
[ "$?" = 1 ]      || ng "$LINENO" #終了ステータスが1なのを確認
[ "${out}" = "" ] || ng "$LINENO" #上の行と入れ替えるとダメ（なぜ？）

out=$(echo | ./plus)              #なにも入力しない
[ "$?" = 1 ]      || ng "$LINENO" #これも異常終了する
[ "${out}" = "" ] || ng "$LINENO"

[ "${res}" = 0 ] && echo OK
exit $res
