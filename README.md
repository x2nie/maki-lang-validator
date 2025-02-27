MAKI as programming language has been used for decades,
but some language features are still mystery (such as `i += 100`).

This project is an atempt to validate whether known syntax is already support or not,
by run the maki compiler (`mc.exe`) with those syntax.

## Assignments
| Operator | Compiled | Usage | Equivalent | Code |
| :------: | :-------: | ----- | ---------- | ---- |
| =  | ✅ | `x = y;`  | `x = y;`        | [eq.m](validator/res/assignment/eq.m#L15) |
| += | ✅ | `x += y;` | `x = x + y;`  | [plus-eq.m](validator/res/assignment/plus-eq.m#L15)  |
| -= | ✅ | `x -= y;` | `x = x - y;`  | [minus-eq.m](validator/res/assignment/minus-eq.m#L15)  |
| /= | ✅ | `x /= y;` | `x = x / y;`  | [slash-eq.m](validator/res/assignment/slash-eq.m#L15)  |
| *= | ✅ | `x *= y;` | `x = x * y;`  | [star-eq.m](validator/res/assignment/star-eq.m#L15)  |
| %= | ✅ | `x %= y;` | `x = x % y;`  | [precent-eq.m](validator/res/assignment/precent-eq.m#L15)  |
| ^= | ✅ | `x ^= y;` | `x = x ^ y;`  | [caret-eq.m](validator/res/assignment/caret-eq.m#L15)  |
| <<= | ✅ | `x <<= y;` | `x = x << y;`  | [lt-lt-eq.m](validator/res/assignment/lt-lt-eq.m#L15)  |
| >>= | ✅ | `x >>= y;` | `x = x >> y;`  | [gt-gt-eq.m](validator/res/assignment/gt-gt-eq.m#L15)  |
| &= | ✅ | `x &= y;` | `x = x & y;`  | [amp-eq.m](validator/res/assignment/amp-eq.m#L15) |
| \|= | ✅ | `x \|= y;` | `x = x \| y;`  | [vbar-eq.m](validator/res/assignment/vbar-eq.m#L15) |
| ~= | ❌ | `x ~= y;` | `x = x ~ y;`  | [tilde-eq.m](validator/res/assignment/tilde-eq.m#L15) |
| = ~ | ❌ | `x = ~y;` | `x = x =~y;`  | [eq-tilde.m](validator/res/assignment/eq-tilde.m#L15) |
| !=  | ✅ | `{ x != y; }` | `x = x ! y;`  | [mark-eq.m](validator/res/assignment/mark-eq.m#L15) |
| = ! | ✅ | `x = !y;` | `x = !y;`  | [eq-mark.m](validator/res/assignment/eq-mark.m#L15) | 
| =!  | ✅ | `x =! y;` | `x = !y;`  | [eqmark.m](validator/res/assignment/eqmark.m#L15) | 
| ? | ❌ | `x =  x ? x : y;` | `if(x != 0) x = x; else x = y;`  |
| ? | ❌ | `x =  x < 0 ? 0 : y;` | `if(x < 0) x = 0; else x = y;`  |
| ? | ❌ | `x =  (x < 0) ? 0 : y;` | `if(x < 0) x = 0; else x = y;`  | [question.m](validator/res/misc/question.m#L15) | 

## Operators 

<details open>
<summary>Int</summary>

| Operator | Compiled | Usage |  Code |
| :------: | :-------: | ----- |  ---- |
| + | ✅ | `x = x + y;` | [int/plus.m](validator/res/binary/int/plus.m#L15) |
| - | ✅ | `x = x - y;` | [int/minus.m](validator/res/binary/int/minus.m#L15) |
| * | ✅ | `x = x * y;` | [int/star.m](validator/res/binary/int/star.m#L15) |
| / | ✅ | `x = x / y;` | [int/slash.m](validator/res/binary/int/slash.m#L15) |
| % | ✅ | `x = x % y;` | [int/precent.m](validator/res/binary/int/precent.m#L15) |
| && | ✅ | `x = x && y;` | [int/amp-amp.m](validator/res/binary/int/amp-amp.m#L15) |
| == | ✅ | `x = x == y;` | [int/eq-eq.m](validator/res/binary/int/eq-eq.m#L15) |
| != | ✅ | `x = x != y;` | [int/mark-eq.m](validator/res/binary/int/mark-eq.m#L15) |
| << | ✅ | `x = x << y;` | [int/lt-lt.m](validator/res/binary/int/lt-lt.m#L15) |
| >> | ✅ | `x = x >> y;` | [int/gt-gt.m](validator/res/binary/int/gt-gt.m#L15) |
| <<< | ❌ | `x = x <<< y;` | [int/lt-lt-lt.m](validator/res/binary/int/lt-lt-lt.m#L15) |
| >>> | ❌ | `x = x >>> y;` | [int/gt-gt-gt.m](validator/res/binary/int/gt-gt-gt.m#L15) |
| \|\| | ✅ | `x = x \|\| y;` | [int/pipe-pipe.m](validator/res/binary/int/pipe-pipe.m#L15) |
</details>

<details>
<summary>Float</summary>

| Operator | Compiled | Usage |  Code |
| :------: | :-------: | ----- |  ---- |
| + | ✅ | `x = x + y;` | [float/plus.m](validator/res/binary/float/plus.m#L15) |
| - | ✅ | `x = x - y;` | [float/minus.m](validator/res/binary/float/minus.m#L15) |
| * | ✅ | `x = x * y;` | [float/star.m](validator/res/binary/float/star.m#L15) |
| / | ✅ | `x = x / y;` | [float/slash.m](validator/res/binary/float/slash.m#L15) |
| % | ❌ | `x = x % y;` | [float/precent.m](validator/res/binary/float/precent.m#L15) |
| && | ✅ | `x = x && y;` | [float/amp-amp.m](validator/res/binary/float/amp-amp.m#L15) |
| == | ✅ | `x = x == y;` | [float/eq-eq.m](validator/res/binary/float/eq-eq.m#L15) |
| != | ✅ | `x = x != y;` | [float/mark-eq.m](validator/res/binary/float/mark-eq.m#L15) |
| << | ❌ | `x = x << y;` | [float/lt-lt.m](validator/res/binary/float/lt-lt.m#L15) |
| >> | ❌ | `x = x >> y;` | [float/gt-gt.m](validator/res/binary/float/gt-gt.m#L15) |
| <<< | ❌ | `x = x <<< y;` | [float/lt-lt-lt.m](validator/res/binary/float/lt-lt-lt.m#L15) |
| >>> | ❌ | `x = x >>> y;` | [float/gt-gt-gt.m](validator/res/binary/float/gt-gt-gt.m#L15) |
| \|\| | ✅ | `x = x \|\| y;` | [float/pipe-pipe.m](validator/res/binary/float/pipe-pipe.m#L15) |
</details>

<details>
<summary>Double</summary>

| Operator | Compiled | Usage |  Code |
| :------: | :-------: | ----- |  ---- |
| + | ✅ | `x = x + y;` | [double/plus.m](validator/res/binary/double/plus.m#L15) |
| - | ✅ | `x = x - y;` | [double/minus.m](validator/res/binary/double/minus.m#L15) |
| * | ✅ | `x = x * y;` | [double/star.m](validator/res/binary/double/star.m#L15) |
| / | ✅ | `x = x / y;` | [double/slash.m](validator/res/binary/double/slash.m#L15) |
| % | ❌ | `x = x % y;` | [double/precent.m](validator/res/binary/double/precent.m#L15) |
| && | ✅ | `x = x && y;` | [double/amp-amp.m](validator/res/binary/double/amp-amp.m#L15) |
| == | ✅ | `x = x == y;` | [double/eq-eq.m](validator/res/binary/double/eq-eq.m#L15) |
| != | ✅ | `x = x != y;` | [double/mark-eq.m](validator/res/binary/double/mark-eq.m#L15) |
| << | ❌ | `x = x << y;` | [double/lt-lt.m](validator/res/binary/double/lt-lt.m#L15) |
| >> | ❌ | `x = x >> y;` | [double/gt-gt.m](validator/res/binary/double/gt-gt.m#L15) |
| <<< | ❌ | `x = x <<< y;` | [double/lt-lt-lt.m](validator/res/binary/double/lt-lt-lt.m#L15) |
| >>> | ❌ | `x = x >>> y;` | [double/gt-gt-gt.m](validator/res/binary/double/gt-gt-gt.m#L15) |
| \|\| | ✅ | `x = x \|\| y;` | [double/pipe-pipe.m](validator/res/binary/double/pipe-pipe.m#L15) |
</details>

<details>
<summary>String</summary>

| Operator | Compiled | Usage |  Code |
| :------: | :-------: | ----- |  ---- |
| + | ✅ | `x = x + y;` | [string/plus.m](validator/res/binary/string/plus.m#L15) |
| - | ❌ | `x = x - y;` | [string/minus.m](validator/res/binary/string/minus.m#L15) |
| * | ❌ | `x = x * y;` | [string/star.m](validator/res/binary/string/star.m#L15) |
| / | ❌ | `x = x / y;` | [string/slash.m](validator/res/binary/string/slash.m#L15) |
| % | ❌ | `x = x % y;` | [string/precent.m](validator/res/binary/string/precent.m#L15) |
| && | ❌ | `x = x && y;` | [string/amp-amp.m](validator/res/binary/string/amp-amp.m#L15) |
| == | ✅ | `x = x == y;` | [string/eq-eq.m](validator/res/binary/string/eq-eq.m#L15) |
| != | ✅ | `x = x != y;` | [string/mark-eq.m](validator/res/binary/string/mark-eq.m#L15) |
| << | ❌ | `x = x << y;` | [string/lt-lt.m](validator/res/binary/string/lt-lt.m#L15) |
| >> | ❌ | `x = x >> y;` | [string/gt-gt.m](validator/res/binary/string/gt-gt.m#L15) |
| <<< | ❌ | `x = x <<< y;` | [string/lt-lt-lt.m](validator/res/binary/string/lt-lt-lt.m#L15) |
| >>> | ❌ | `x = x >>> y;` | [string/gt-gt-gt.m](validator/res/binary/string/gt-gt-gt.m#L15) |
| \|\| | ❌ | `x = x \|\| y;` | [string/pipe-pipe.m](validator/res/binary/string/pipe-pipe.m#L15) |
</details>

<details>
<summary>Boolean</summary>

| Operator | Compiled | Usage |  Code |
| :------: | :-------: | ----- |  ---- |
| + | ✅ | `x = x + y;` | [boolean/plus.m](validator/res/binary/boolean/plus.m#L15) |
| - | ✅ | `x = x - y;` | [boolean/minus.m](validator/res/binary/boolean/minus.m#L15) |
| * | ✅ | `x = x * y;` | [boolean/star.m](validator/res/binary/boolean/star.m#L15) |
| / | ✅ | `x = x / y;` | [boolean/slash.m](validator/res/binary/boolean/slash.m#L15) |
| % | ❌ | `x = x % y;` | [boolean/precent.m](validator/res/binary/boolean/precent.m#L15) |
| && | ✅ | `x = x && y;` | [boolean/amp-amp.m](validator/res/binary/boolean/amp-amp.m#L15) |
| == | ✅ | `x = x == y;` | [boolean/eq-eq.m](validator/res/binary/boolean/eq-eq.m#L15) |
| != | ✅ | `x = x != y;` | [boolean/mark-eq.m](validator/res/binary/boolean/mark-eq.m#L15) |
| << | ❌ | `x = x << y;` | [boolean/lt-lt.m](validator/res/binary/boolean/lt-lt.m#L15) |
| >> | ❌ | `x = x >> y;` | [boolean/gt-gt.m](validator/res/binary/boolean/gt-gt.m#L15) |
| <<< | ❌ | `x = x <<< y;` | [boolean/lt-lt-lt.m](validator/res/binary/boolean/lt-lt-lt.m#L15) |
| >>> | ❌ | `x = x >>> y;` | [boolean/gt-gt-gt.m](validator/res/binary/boolean/gt-gt-gt.m#L15) |
| \|\| | ✅ | `x = x \|\| y;` | [boolean/pipe-pipe.m](validator/res/binary/boolean/pipe-pipe.m#L15) |
</details>

## Unary operation

<details>
<summary>Int</summary>

| Operator | Name | Compiled | Usage |  Code |
| :------: | ---- | :------: | ----- |  ---- |
| !y | Not | ✅ | `x = !y;` | [int/mark.m](validator/res/unary/int/mark.m#L15) |
| ~y | Bits Not | ❌ | `x = ~y;` | [int/tilde.m](validator/res/unary/int/tilde.m#L15) |
| -y | Negative | ✅ | `x = -y;` | [int/minus.m](validator/res/unary/int/minus.m#L15) |
| y++ | postinc | ✅ | `x = y++;` | [int/postinc.m](validator/res/unary/int/postinc.m#L15) |
| y-- | postdec | ✅ | `x = y--;` | [int/postdec.m](validator/res/unary/int/postdec.m#L15) |
| ++y | preinc | ✅ | `x = ++y;` | [int/preinc.m](validator/res/unary/int/preinc.m#L15) |
| --y | predec | ❌ | `x = --y;` | [int/predec.m](validator/res/unary/int/predec.m#L15) |
</details>

<details>
<summary>Float</summary>

| Operator | Name | Compiled | Usage |  Code |
| :------: | ---- | :------: | ----- |  ---- |
| !y | Not | ✅ | `x = !y;` | [float/mark.m](validator/res/unary/float/mark.m#L15) |
| ~y | Bits Not | ❌ | `x = ~y;` | [float/tilde.m](validator/res/unary/float/tilde.m#L15) |
| -y | Negative | ✅ | `x = -y;` | [float/minus.m](validator/res/unary/float/minus.m#L15) |
| y++ | postinc | ✅ | `x = y++;` | [float/postinc.m](validator/res/unary/float/postinc.m#L15) |
| y-- | postdec | ✅ | `x = y--;` | [float/postdec.m](validator/res/unary/float/postdec.m#L15) |
| ++y | preinc | ✅ | `x = ++y;` | [float/preinc.m](validator/res/unary/float/preinc.m#L15) |
| --y | predec | ❌ | `x = --y;` | [float/predec.m](validator/res/unary/float/predec.m#L15) |
</details>

<details>
<summary>Double</summary>

| Operator | Name | Compiled | Usage |  Code |
| :------: | ---- | :------: | ----- |  ---- |
| !y | Not | ✅ | `x = !y;` | [double/mark.m](validator/res/unary/double/mark.m#L15) |
| ~y | Bits Not | ❌ | `x = ~y;` | [double/tilde.m](validator/res/unary/double/tilde.m#L15) |
| -y | Negative | ✅ | `x = -y;` | [double/minus.m](validator/res/unary/double/minus.m#L15) |
| y++ | postinc | ✅ | `x = y++;` | [double/postinc.m](validator/res/unary/double/postinc.m#L15) |
| y-- | postdec | ✅ | `x = y--;` | [double/postdec.m](validator/res/unary/double/postdec.m#L15) |
| ++y | preinc | ✅ | `x = ++y;` | [double/preinc.m](validator/res/unary/double/preinc.m#L15) |
| --y | predec | ❌ | `x = --y;` | [double/predec.m](validator/res/unary/double/predec.m#L15) |
</details>

<details>
<summary>String</summary>

| Operator | Name | Compiled | Usage |  Code |
| :------: | ---- | :------: | ----- |  ---- |
| !y | Not | ❌ | `x = !y;` | [string/mark.m](validator/res/unary/string/mark.m#L15) |
| ~y | Bits Not | ❌ | `x = ~y;` | [string/tilde.m](validator/res/unary/string/tilde.m#L15) |
| -y | Negative | ✅ | `x = -y;` | [string/minus.m](validator/res/unary/string/minus.m#L15) |
| y++ | postinc | ❌ | `x = y++;` | [string/postinc.m](validator/res/unary/string/postinc.m#L15) |
| y-- | postdec | ❌ | `x = y--;` | [string/postdec.m](validator/res/unary/string/postdec.m#L15) |
| ++y | preinc | ❌ | `x = ++y;` | [string/preinc.m](validator/res/unary/string/preinc.m#L15) |
| --y | predec | ❌ | `x = --y;` | [string/predec.m](validator/res/unary/string/predec.m#L15) |
</details>

<details>
<summary>Boolean</summary>

| Operator | Name | Compiled | Usage |  Code |
| :------: | ---- | :------: | ----- |  ---- |
| !y | Not | ✅ | `x = !y;` | [boolean/mark.m](validator/res/unary/boolean/mark.m#L15) |
| ~y | Bits Not | ❌ | `x = ~y;` | [boolean/tilde.m](validator/res/unary/boolean/tilde.m#L15) |
| -y | Negative | ✅ | `x = -y;` | [boolean/minus.m](validator/res/unary/boolean/minus.m#L15) |
| y++ | postinc | ✅ | `x = y++;` | [boolean/postinc.m](validator/res/unary/boolean/postinc.m#L15) |
| y-- | postdec | ✅ | `x = y--;` | [boolean/postdec.m](validator/res/unary/boolean/postdec.m#L15) |
| ++y | preinc | ✅ | `x = ++y;` | [boolean/preinc.m](validator/res/unary/boolean/preinc.m#L15) |
| --y | predec | ❌ | `x = --y;` | [boolean/predec.m](validator/res/unary/boolean/predec.m#L15) |
</details>
