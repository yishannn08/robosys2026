#!/bin/bash -xv
# SPDX-FileCopyrightText: 2026 CHAI YI SHAN
# SPDX-License-Identifier: BSD-3-Clause

ng () {
	echo "${1}行目が違うよ"
	res=1
}

res=0

out=$(printf "task,status,due\nReport,done,2026-11-01\nCode,todo,2099-12-31\nCode,todo,\n" | ./taskchk)
echo "${out}" | grep -q "Total     : 3" || ng "$LINENO"
echo "${out}" | grep -q "Completed : 1" || ng "$LINENO"
echo "${out}" | grep -q "Remaining : 2" || ng "$LINENO"
echo "${out}" | grep -q "Duplicates: 1" || ng "$LINENO"
echo "${out}" | grep -q "No due    : 1" || ng "$LINENO"
echo "${out}" | grep -q "Overdue   : 0" || ng "$LINENO"

out_overdue=$(printf "task,status,due\nOld task,todo,2020-01-01\n" | ./taskchk)
echo "${out_overdue}" | grep -q "Overdue   : 1" || ng "$LINENO"
echo "${out_overdue}" | grep -q -- "- Old task" || ng "$LINENO"

out=$(printf "" | ./taskchk 2>/dev/null)
[ "$?" = 1 ] || ng "$LINENO"
[ "${out}" = "" ] || ng "$LINENO"

out=$(printf "name,state\nA,done\n" | ./taskchk 2>/dev/null)
[ "$?" = 1 ] || ng "$LINENO"
[ "${out}" = "" ] || ng "$LINENO"

out=$(printf "task,status,due\n,todo,2026-12-01\n" | ./taskchk 2>/dev/null)
[ "$?" = 1 ] || ng "$LINENO"
[ "${out}" = "" ] || ng "$LINENO"

out=$(printf "task,status,due\nA,todo,2026-99-99\n" | ./taskchk 2>/dev/null)
[ "$?" = 1 ] || ng "$LINENO"
[ "${out}" = "" ] || ng "$LINENO"

[ "${res}" = 0 ] && echo "OK"
exit $res
