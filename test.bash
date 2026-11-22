#!/bin/bash -xv
# SPDX-FileCopyrightText: 2026 CHAI YI SHAN
# SPDX-License-Identifier: BSD-3-Clause

ng () {
	echo "${1}行目が違うよ"
	res=1
}

res=0

### 正常系テスト（马来语 -> 日语） ###
out=$(printf "kucing\nnasi lemak\n" | ./doneberry)
[ "$?" = 0 ] || ng "$LINENO"
echo "${out}" | grep -q "^kucing -> 猫$" || ng "$LINENO"
echo "${out}" | grep -q "^nasi lemak -> " || ng "$LINENO"

### 正常系テスト（日语 -> 马来语） ###
out=$(echo "ありがとうございます" | ./doneberry)
[ "$?" = 0 ] || ng "$LINENO"
echo "${out}" | grep -qi "^ありがとうございます -> terima kasih" || ng "$LINENO"

### 異常系テスト（空输入） ###
out=$(printf "" | ./doneberry 2>/dev/null)
[ "$?" = 1 ] || ng "$LINENO"
[ "${out}" = "" ] || ng "$LINENO"

### 異常系テスト（纯数字/无字母） ###
out=$(echo "12345" | ./doneberry 2>/dev/null)
[ "$?" = 1 ] || ng "$LINENO"
[ "${out}" = "" ] || ng "$LINENO"

### 異常系テスト（多余命令行参数） ###
out=$(echo "kucing" | ./doneberry extra_arg 2>/dev/null)
[ "$?" = 1 ] || ng "$LINENO"
[ "${out}" = "" ] || ng "$LINENO"

[ "${res}" = 0 ] && echo "OK"
exit $res
