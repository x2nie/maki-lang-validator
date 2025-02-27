MAKI as programming language has been used for decades,
but some language features are still mystery (such as `i += 100`).

This project is an atempt to validate whether known syntax is already support or not,
by run the maki compiler (`mc.exe`) with those syntax.

## Assignments
| Operator | Supported | Usage | Equivalent | Code |
| :------: | :-------: | ----- | ---------- | ---- |
| =  | ✅ | `x = y;`  | `x = y;`        | [eq.m](res/assignment/eq.m) |
| += | ✅ | `x += y;` | `x = x + y;`    |
| -= | ✅ | `x -= y;` | `x = x - y;`  |
| /= | ✅ | `x /= y;` | `x = x / y;`  |
| *= | ✅ | `x *= y;` | `x = x * y;`  |
| %= | ✅ | `x %= y;` | `x = x % y;`  |
| ^= | ✅ | `x ^= y;` | `x = x ^ y;`  |
| <<= | ✅ | `x <<= y;` | `x = x << y;`  |
| >>= | ✅ | `x >>= y;` | `x = x >> y;`  |
| &= | ✅ | `x &= y;` | `x = x & y;`  |
| &VerticalLine;= | ✅ | `x \|= y;` | `x = x \| y;`  |
| ~= | ❌ | `x ~= y;` | `x = x ~ y;`  |
| = ~ | ❌ | `x = ~y;` | `x = x =~y;`  |
| !=  | ✅ | `{ x != y; }` | `x = x ! y;`  |
| = ! | ✅ | `x = !y;` | `x = !y;`  |
| =!  | ✅ | `x =! y;` | `x = !y;`  |
| ? | ❌ | `x =  x ? x : y;` | `if(x != 0) x = x; else x = y;`  |
| ? | ❌ | `x =  x < 0 ? 0 : y;` | `if(x < 0) x = 0; else x = y;`  |
| ? | ❌ | `x =  (x < 0) ? 0 : y;` | `if(x < 0) x = 0; else x = y;`  |