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
| &VerticalLine;= | ✅ | `x \|= y;` | `x = x \| y;`  | [vbar-eq.m](validator/res/assignment/vbar-eq.m#L15) |
| ~= | ❌ | `x ~= y;` | `x = x ~ y;`  | [tilde-eq.m](validator/res/assignment/tilde-eq.m#L15) |
| = ~ | ❌ | `x = ~y;` | `x = x =~y;`  | [eq-tilde.m](validator/res/assignment/eq-tilde.m#L15) |
| !=  | ✅ | `{ x != y; }` | `x = x ! y;`  | [mark-eq.m](validator/res/assignment/mark-eq.m#L15) |
| = ! | ✅ | `x = !y;` | `x = !y;`  | [eq-mark.m](validator/res/assignment/eq-mark.m#L15) | 
| =!  | ✅ | `x =! y;` | `x = !y;`  | [eqmark.m](validator/res/assignment/eqmark.m#L15) | 
| ? | ❌ | `x =  x ? x : y;` | `if(x != 0) x = x; else x = y;`  |
| ? | ❌ | `x =  x < 0 ? 0 : y;` | `if(x < 0) x = 0; else x = y;`  |
| ? | ❌ | `x =  (x < 0) ? 0 : y;` | `if(x < 0) x = 0; else x = y;`  | [question.m](validator/res/misc/question.m#L15) | 