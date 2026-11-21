#!/bin/bash
# SPDX-FileCopyrightText: 2026 CHAI YI SHAN
# SPDX-License-Identifier: BSD-3-Clause

ng () {
	echo "${1}行目が違うよ"
	res=1
}

res=0

out=$(printf "Merry Christmas\n" | ./xtree)
echo "${out}" | grep -q "★" || ng "$LINENO"
echo "${out}" | grep -q "| Merry Christmas |" || ng "$LINENO"

out_snow=$(printf "Robosys 2026\n" | ./xtree -s)
echo "${out_snow}" | grep -q "| Robosys 2026 |" || ng "$LINENO"

out_color=$(printf "Hello\n" | ./xtree -c)
printf "%s" "${out_color}" | grep -q $'\033\[' || ng "$LINENO"

out=$(printf "" | ./xtree 2>/dev/null)
[ "$?" = 1 ] || ng "$LINENO"
[ "${out}" = "" ] || ng "$LINENO"

out=$(printf "   \n" | ./xtree 2>/dev/null)
[ "$?" = 1 ] || ng "$LINENO"
[ "${out}" = "" ] || ng "$LINENO"

out=$(printf "Hello\n" | ./xtree -x 2>/dev/null)
[ "$?" = 1 ] || ng "$LINENO"
[ "${out}" = "" ] || ng "$LINENO"

[ "${res}" = 0 ] && echo "OK"
exit $res
