import os
from visit_maki import find_files_with_extension

SYMBOL = {
    'star' : '*',
    'eq' : '=',
    'slash' : '/',
    'precent' : '%',
    'plus' : '+',
    'minus' : '-',
    'amp' : '&',
    'lt' : '<',
    'gt' : '>',
    'caret' : '^',
    'tilde' : '~',
    'pipe' : '|',
    'mark' : '!',
    'postinc': 'y++',
    'postdec': 'y--',
    'preinc': '++y',
    'predec': '--y',
}

if 1: #* binary
    typs = {'int':[], 'float':[], 'double':[], 'string':[], 'boolean':[]}
    for pathfile in find_files_with_extension('validator/res/binary', '.m'):
        compiled = os.path.exists(f'{pathfile}aki')
        # print(compiled, pathfile)

        path,file = os.path.split(pathfile)
        _, type = os.path.split(path)
        name,ext = os.path.splitext(file)

        op = ''
        for part in name.split('-'):
            op += SYMBOL[part]
            
        status = '✅' if compiled else '❌'
        op = op.replace('|', '\\|')
        row = f"| {op} | {status} | `x = x {op} y;` | [{type}/{file}]({pathfile}#L15) |"
        print(row)
        typs[type].append(row)

    print()

    order = ['+', '-', '*', '/', '%', '^', '~', '&', '|',  '&&', '||', '==', '!=', '<<', '>>', '<<<', '>>>']
    def get_sort_key(item):
        # operator = item[0]  # Ambil simbol operator dari tuple
        operator = item.strip(' |').split('|')[0].strip()  # Ambil simbol operator dari tuple
        return order.index(operator) if operator in order else len(order)
    
    for typ,array in typs.items():
        print('<details>')
        # ''.title()
        print(f'<summary>{typ.title()}</summary>')
        # print(type)
        print()
        print('| Operator | Compiled | Usage |  Code |')
        print('| :------: | :-------: | ----- |  ---- |')
        #? urutkan dulu sedemikian rupa
        array = sorted(array, key=get_sort_key)
        for row in array:
            print(row)
        print('</details>')
        print()

if 0: #* unary
    SYMBOL = {
        'star' : '*',
        'eq' : '=',
        'slash' : '/',
        'precent' : '%',
        'plus' : '+',
        'minus' : '-y',
        'amp' : '&',
        'lt' : '<',
        'gt' : '>',
        'caret' : '^',
        'tilde' : '~y',
        'pipe' : '|y',
        'mark' : '!y',
        'postinc': 'y++',
        'postdec': 'y--',
        'preinc': '++y',
        'predec': '--y',
    }
    typs = {'int':[], 'float':[], 'double':[], 'string':[], 'boolean':[]}
    for pathfile in find_files_with_extension('validator/res/unary', '.m'):
        compiled = os.path.exists(f'{pathfile}aki')
        # print(compiled, pathfile)

        path,file = os.path.split(pathfile)
        _, type = os.path.split(path)
        name,ext = os.path.splitext(file)

        op = ''
        for part in name.split('-'):
            op += SYMBOL[part]
            
        status = '✅' if compiled else '❌'
        row = f"| {op} | {name} | {status} | `x = {op};` | [{type}/{file}]({pathfile}#L15) |"
        print(row)
        typs[type].append(row)

    print()
    

    order = ['+', '-', '*', '/', '%', '&&', '||', '==', '!=', '<<', '>>', '<<<', '>>>']
    order = "!y ~y -y y++ y-- ++y --y".split(' ')
    def get_sort_key(item):
        # operator = item[0]  # Ambil simbol operator dari tuple
        operator = item.strip(' |').split('|')[0].strip()  # Ambil simbol operator dari tuple
        return order.index(operator) if operator in order else len(order)
    
    for typ,array in typs.items():
        print('<details>')
        # ''.title()
        print(f'<summary>{typ.title()}</summary>')
        # print(type)
        print()
        print('| Operator | Name | Compiled | Usage |  Code |')
        print('| :------: | ---- | :------: | ----- |  ---- |')
        #? urutkan dulu sedemikian rupa
        array = sorted(array, key=get_sort_key)
        for row in array:
            print(row)
        print('</details>')
        print()
