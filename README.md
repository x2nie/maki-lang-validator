MAKI as programming language has been used for decades,
but some language features are still mystery (such as `i += 100`).

This project is an atempt to validate whether known syntax is already support or not,
by run the maki compiler (`mc.exe`) with those syntax.

## Assignments
| Operator | Supported | Sample syntax | Equivalent |
| -------- | --------- | ------------- | ---------- |
| =  | ✅ | `x = y;`  | `x = y;`   |
| += | ✅ | `x += y;` | `x = x + y;`  |
| -= | ✅ | `x -= y;` | `x = x - y;`  |
| /= | ✅ | `x /= y;` | `x = x / y;`  |
| *= | ✅ | `x *= y;` | `x = x * y;`  |
| %= | ✅ | `x %= y;` | `x = x % y;`  |
| ^= | ✅ | `x ^= y;` | `x = x ^ y;`  |
| <<= | ✅ | `x <<= y;` | `x = x << y;`  |
| >>= | ✅ | `x >>= y;` | `x = x >> y;`  |
| &= | ✅ | `x &= y;` | `x = x & y;`  |
| &VerticalLine;= | ✅ | x &VerticalLine;= y; | x = x &VerticalLine; y;  |
| ~= | ❌ | `x ~= y;` | `x = x ~ y;`  |
| = ~ | ❌ | `x = ~y;` | x = x =~y;`  |
| !=  | ✅ | `{ x != y; }` | `x = x ! y;`  |
| = ! | ✅ | `x = !y;` | x = !y;`  |
| =!  | ✅ | `x =! y;` | `x = !y;`  |
| ? | ❌ | `x =  x < 0 ? 0 : y;` | `if(x < 0) x = 0; else x = y;`  |