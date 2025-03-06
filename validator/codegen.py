import os
import subprocess
from run import compile

CURDIR = os.path.dirname(__file__)
os.chdir(CURDIR)


NAMES = {
    '*': 'star',
    '=': 'eq',
    '/': 'slash',
    '%': 'precent',
    '+': 'plus',
    '-': 'minus',
    '&': 'amp',
    '<': 'lt',
    '>': 'gt',
    '^': 'caret',
    '~': 'tilde',
    '|': 'pipe',
    '!': 'mark',
    'y++': 'postinc',
    'y--': 'postdec',
    '++y': 'preinc',
    '--y': 'predec',
}
def get_name(symbols):
    result = NAMES.get(symbols)
    if result: 
        return result
    else:
        symbols = symbols.strip('y')

    result = ''
    for s in symbols:
        result += NAMES.get(s,f'-unknown-') 
        result += '-'
    result = result.strip('-')
    return result

tpl = '''
#define MC_TARGET "Test"
#define VCPU_VERSION 2

extern class @{51654971-0D87-4a51-91E3-A6B53235F3E7}@ @{00000000-0000-0000-0000-000000000000}@ Object;
extern class @{D6F50F64-93FA-49b7-93F1-BA66EFAE3E98}@ Object _predecl System;


function int coding(int, int);

.CODE

coding(int x, int y)
{
    %s
    return x;
}
'''

if 0:
    assignments = "*= /= %= += -= <<= >>= &= |= ^= = ~= !=".split(' ')
    for op in assignments:
        name = get_name(op)
        # print(name)

        stat = f"x {op} y;"
        print(f"| {op} | ✅ | `{stat}` |")
        # print(tpl % stat)

        mpath = f'res/assignment/{name}.m'
        with open(mpath, 'w') as f:
            f.write(tpl % stat)

        compile(mpath)
        # break
if 1: #? Binary
    operators = "+ - * / % ^ ~ & | && || == != << >> <<< >>>".split(' ')
    for op in operators:
        name = get_name(op)
        # print(name)

        for type in ['int', 'float', 'double', 'boolean', 'string']:

            stat = f"x = x {op} y;"
            print(f"| {op} | ✅ | `{stat}` |")
            # print(tpl % stat)

            mpath = f'res/binary/{type}/{name}.m'
            os.makedirs(os.path.dirname(mpath), exist_ok=True)

            with open(mpath, 'w') as f:
                content = tpl % stat
                content = content.replace('int', type)
                f.write(content)

            compile(mpath)
        # break

if 0: #? Unary
    operators = "!y ~y -y y++ y-- ++y --y".split(' ')
    for expression in operators:
        name = get_name(expression)
        op = expression.strip('y')
        # name = get_name(op)
        # print(name)

        for type in ['int', 'float', 'double', 'boolean', 'string']:

            stat = f"x = {expression};"
            print(f"| {op} | {name} | ✅ | `{stat}` |")
            # print(tpl % stat)
            # continue

            mpath = f'res/unary/{type}/{name}.m'
            os.makedirs(os.path.dirname(mpath), exist_ok=True)

            with open(mpath, 'w') as f:
                content = tpl % stat
                content = content.replace('int', type)
                f.write(content)

            #* recompile,
            if not os.path.exists(f'{mpath}aki'):
                compile(mpath)
        # break