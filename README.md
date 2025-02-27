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
| + | ✅ | `x = x + y;` | [plus.m](validator/res/binary/int/plus.m#L15) |
| - | ✅ | `x = x - y;` | [minus.m](validator/res/binary/int/minus.m#L15) |
| * | ✅ | `x = x * y;` | [star.m](validator/res/binary/int/star.m#L15) |
| / | ✅ | `x = x / y;` | [slash.m](validator/res/binary/int/slash.m#L15) |
| % | ✅ | `x = x % y;` | [precent.m](validator/res/binary/int/precent.m#L15) |
| && | ✅ | `x = x && y;` | [amp-amp.m](validator/res/binary/int/amp-amp.m#L15) |
| == | ✅ | `x = x == y;` | [eq-eq.m](validator/res/binary/int/eq-eq.m#L15) |
| != | ✅ | `x = x != y;` | [mark-eq.m](validator/res/binary/int/mark-eq.m#L15) |
| << | ✅ | `x = x << y;` | [lt-lt.m](validator/res/binary/int/lt-lt.m#L15) |
| >> | ✅ | `x = x >> y;` | [gt-gt.m](validator/res/binary/int/gt-gt.m#L15) |
| <<< | ❌ | `x = x <<< y;` | [lt-lt-lt.m](validator/res/binary/int/lt-lt-lt.m#L15) |
| >>> | ❌ | `x = x >>> y;` | [gt-gt-gt.m](validator/res/binary/int/gt-gt-gt.m#L15) |
| || | ✅ | `x = x || y;` | [pipe-pipe.m](validator/res/binary/int/pipe-pipe.m#L15) |
</details>

<details>
<summary>Float</summary>

| Operator | Compiled | Usage |  Code |
| :------: | :-------: | ----- |  ---- |
| + | ✅ | `x = x + y;` | [plus.m](validator/res/binary/float/plus.m#L15) |
| - | ✅ | `x = x - y;` | [minus.m](validator/res/binary/float/minus.m#L15) |
| * | ✅ | `x = x * y;` | [star.m](validator/res/binary/float/star.m#L15) |
| / | ✅ | `x = x / y;` | [slash.m](validator/res/binary/float/slash.m#L15) |
| % | ❌ | `x = x % y;` | [precent.m](validator/res/binary/float/precent.m#L15) |
| && | ✅ | `x = x && y;` | [amp-amp.m](validator/res/binary/float/amp-amp.m#L15) |
| == | ✅ | `x = x == y;` | [eq-eq.m](validator/res/binary/float/eq-eq.m#L15) |
| != | ✅ | `x = x != y;` | [mark-eq.m](validator/res/binary/float/mark-eq.m#L15) |
| << | ❌ | `x = x << y;` | [lt-lt.m](validator/res/binary/float/lt-lt.m#L15) |
| >> | ❌ | `x = x >> y;` | [gt-gt.m](validator/res/binary/float/gt-gt.m#L15) |
| <<< | ❌ | `x = x <<< y;` | [lt-lt-lt.m](validator/res/binary/float/lt-lt-lt.m#L15) |
| >>> | ❌ | `x = x >>> y;` | [gt-gt-gt.m](validator/res/binary/float/gt-gt-gt.m#L15) |
| || | ✅ | `x = x || y;` | [pipe-pipe.m](validator/res/binary/float/pipe-pipe.m#L15) |
</details>

<details>
<summary>Double</summary>

| Operator | Compiled | Usage |  Code |
| :------: | :-------: | ----- |  ---- |
| + | ✅ | `x = x + y;` | [plus.m](validator/res/binary/double/plus.m#L15) |
| - | ✅ | `x = x - y;` | [minus.m](validator/res/binary/double/minus.m#L15) |
| * | ✅ | `x = x * y;` | [star.m](validator/res/binary/double/star.m#L15) |
| / | ✅ | `x = x / y;` | [slash.m](validator/res/binary/double/slash.m#L15) |
| % | ❌ | `x = x % y;` | [precent.m](validator/res/binary/double/precent.m#L15) |
| && | ✅ | `x = x && y;` | [amp-amp.m](validator/res/binary/double/amp-amp.m#L15) |
| == | ✅ | `x = x == y;` | [eq-eq.m](validator/res/binary/double/eq-eq.m#L15) |
| != | ✅ | `x = x != y;` | [mark-eq.m](validator/res/binary/double/mark-eq.m#L15) |
| << | ❌ | `x = x << y;` | [lt-lt.m](validator/res/binary/double/lt-lt.m#L15) |
| >> | ❌ | `x = x >> y;` | [gt-gt.m](validator/res/binary/double/gt-gt.m#L15) |
| <<< | ❌ | `x = x <<< y;` | [lt-lt-lt.m](validator/res/binary/double/lt-lt-lt.m#L15) |
| >>> | ❌ | `x = x >>> y;` | [gt-gt-gt.m](validator/res/binary/double/gt-gt-gt.m#L15) |
| || | ✅ | `x = x || y;` | [pipe-pipe.m](validator/res/binary/double/pipe-pipe.m#L15) |
</details>

<details>
<summary>String</summary>

| Operator | Compiled | Usage |  Code |
| :------: | :-------: | ----- |  ---- |
| + | ✅ | `x = x + y;` | [plus.m](validator/res/binary/string/plus.m#L15) |
| - | ❌ | `x = x - y;` | [minus.m](validator/res/binary/string/minus.m#L15) |
| * | ❌ | `x = x * y;` | [star.m](validator/res/binary/string/star.m#L15) |
| / | ❌ | `x = x / y;` | [slash.m](validator/res/binary/string/slash.m#L15) |
| % | ❌ | `x = x % y;` | [precent.m](validator/res/binary/string/precent.m#L15) |
| && | ❌ | `x = x && y;` | [amp-amp.m](validator/res/binary/string/amp-amp.m#L15) |
| == | ✅ | `x = x == y;` | [eq-eq.m](validator/res/binary/string/eq-eq.m#L15) |
| != | ✅ | `x = x != y;` | [mark-eq.m](validator/res/binary/string/mark-eq.m#L15) |
| << | ❌ | `x = x << y;` | [lt-lt.m](validator/res/binary/string/lt-lt.m#L15) |
| >> | ❌ | `x = x >> y;` | [gt-gt.m](validator/res/binary/string/gt-gt.m#L15) |
| <<< | ❌ | `x = x <<< y;` | [lt-lt-lt.m](validator/res/binary/string/lt-lt-lt.m#L15) |
| >>> | ❌ | `x = x >>> y;` | [gt-gt-gt.m](validator/res/binary/string/gt-gt-gt.m#L15) |
| || | ❌ | `x = x || y;` | [pipe-pipe.m](validator/res/binary/string/pipe-pipe.m#L15) |
</details>

<details>
<summary>Boolean</summary>

| Operator | Compiled | Usage |  Code |
| :------: | :-------: | ----- |  ---- |
| + | ✅ | `x = x + y;` | [plus.m](validator/res/binary/boolean/plus.m#L15) |
| - | ✅ | `x = x - y;` | [minus.m](validator/res/binary/boolean/minus.m#L15) |
| * | ✅ | `x = x * y;` | [star.m](validator/res/binary/boolean/star.m#L15) |
| / | ✅ | `x = x / y;` | [slash.m](validator/res/binary/boolean/slash.m#L15) |
| % | ❌ | `x = x % y;` | [precent.m](validator/res/binary/boolean/precent.m#L15) |
| && | ✅ | `x = x && y;` | [amp-amp.m](validator/res/binary/boolean/amp-amp.m#L15) |
| == | ✅ | `x = x == y;` | [eq-eq.m](validator/res/binary/boolean/eq-eq.m#L15) |
| != | ✅ | `x = x != y;` | [mark-eq.m](validator/res/binary/boolean/mark-eq.m#L15) |
| << | ❌ | `x = x << y;` | [lt-lt.m](validator/res/binary/boolean/lt-lt.m#L15) |
| >> | ❌ | `x = x >> y;` | [gt-gt.m](validator/res/binary/boolean/gt-gt.m#L15) |
| <<< | ❌ | `x = x <<< y;` | [lt-lt-lt.m](validator/res/binary/boolean/lt-lt-lt.m#L15) |
| >>> | ❌ | `x = x >>> y;` | [gt-gt-gt.m](validator/res/binary/boolean/gt-gt-gt.m#L15) |
| || | ✅ | `x = x || y;` | [pipe-pipe.m](validator/res/binary/boolean/pipe-pipe.m#L15) |
</details>