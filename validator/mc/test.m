//#include "std2.mi"


#define MC_TARGET "Test"
#define VCPU_VERSION 2

extern class @{51654971-0D87-4a51-91E3-A6B53235F3E7}@ @{00000000-0000-0000-0000-000000000000}@ Object;
extern class @{D6F50F64-93FA-49b7-93F1-BA66EFAE3E98}@ Object _predecl System;
extern class @{B2023AB5-434D-4ba1-BEAE-59637503F3C6}@ Object &List;

extern System.getInt();
extern System.onStart();
extern int List.getItem();

function int test(int, int);

Global int s;
Global System t;

.CODE

System.onStart()
{
	int i = 1;
	do
	{
		i = 0;
	} while (i);
}

test(int x, int y)
{
	return 5;
}