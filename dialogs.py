#! /usr/bin/python
#-*- coding: utf-8 -*- 
a=input("Cien. liet., lūdzu, ievadi skaitli: ")
# 3. pythonā visi input rezultāti ir ar str datu tipu, tāpēc ievadītā lieluma datu tips vēlāk ir jāpārveido
a=int(a)
# python valoda balstās uz C valotas => print strādā līdzīgi printf - www.cplusplus.com/reference/cstdio/printf/
print("Liet., Tu esi ievadījis skaitli: %d"%(a))
aa = a * a
print("Tavs skaitlis kvadrātā ir: %d"%(aa))
