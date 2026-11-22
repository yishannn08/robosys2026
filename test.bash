#!/bin/bash -xv
# SPDX-FileCopyrightText: 2026 CHAI YI SHAN
# SPDX-License-Identifier: BSD-3-Clause

ng () {
	echo "${1}行目が違うよ"
	res=1
}

res=0

out=$(printf "kucing\nnasi lemak\n" | ./doneberry)
[ "$?" = 0 ] || ng "$LINENO"
echo "${out}" | grep -q "^kucing -> 猫$" || ng "$LINENO"
echo "${out}" | grep -q "^nasi lemak -> " || ng "$LINENO"

out=$(echo "ありがとうございます" | ./doneberry)
[ "$?" = 0 ] || ng "$LINENO"
echo "${out}" | grep -qi "^ありがとうございます -> terima kasih" || ng "$LINENO"

out=$(printf "" | ./doneberry 2>/dev/null)
[ "$?" = 1 ] || ng "$LINENO"
[ "${out}" = "" ] || ng "$LINENO"

out=$(echo "12345" | ./doneberry 2>/dev/null)
[ "$?" = 1 ] || ng "$LINENO"
[ "${out}" = "" ] || ng "$LINENO"

out=$(echo "kucing" | ./doneberry extra_arg 2>/dev/null)
[ "$?" = 1 ] || ng "$LINENO"
[ "${out}" = "" ] || ng "$LINENO"

[ "${res}" = 0 ] && echo "OK"
exit $res
