
#define MC_TARGET "Test"
#define VCPU_VERSION 2

extern class @{51654971-0D87-4a51-91E3-A6B53235F3E7}@ @{00000000-0000-0000-0000-000000000000}@ Object;
extern class @{D6F50F64-93FA-49b7-93F1-BA66EFAE3E98}@ Object _predecl System;


function string coding(string, string);

.CODE

coding(string x, string y)
{
    x = ++y;
    return x;
}
