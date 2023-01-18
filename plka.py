def func1(arg1, arg2):
    var6 = func2(arg2, arg1)
    def func4(arg7, arg8):
        var9 = func7()
        var12 = class8()
        for var13 in xrange(32):
            var14 = var12.func9
            var14(arg1, arg1)
        var15 = func12()
        var16 = arg1 ^ var9
        var17 = 1192420384 ^ 334 | 567 ^ var16
        var18 = -93458023 | arg2 - 426 - arg2
        var19 = (arg2 & var18) | arg7
        var20 = arg1 | var9 ^ (var19 | arg7)
        var21 = (arg7 & var19 & arg7) ^ var15
        var22 = var18 | ((var19 | arg7) + var19)
        var23 = var17 ^ (var6 + var17 ^ var19)
        var24 = var6 & (var9 - var16 | var22)
        var25 = var20 - 61 + var23 & arg2
        var26 = ((arg2 ^ arg2) & var15) | var19
        var27 = ((var21 - arg7) & var24) + var21
        var28 = var21 ^ (var27 & var24)
        var29 = 939850190 + var18 | var26 + var22
        var30 = var15 & var27
        var31 = 1349450903 | (var24 & var29)
        var32 = var27 & var26
        var33 = (var27 & var22 + var15) - arg1
        var34 = (var15 ^ 1464430516 & arg2) + var6
        var35 = arg8 - 614
        result = var28 + var20
        return result
    var36 = func4(arg1, arg2)
    var37 = -1886132724 | var6 & var6
    var38 = var37 + var36 | 800
    if var6 < var37:
        var39 = var38 & arg1 + var36 | var36
    else:
        var39 = var6 ^ 654 | (arg1 & var36)
    var40 = -865 | arg2 + var36 ^ var38
    var41 = var40 & var37
    var42 = var37 | -1039438982 | var37 - var6
    if var42 < arg2:
        var43 = var38 | var6 & var38 & var37
    else:
        var43 = 353 - var38
    var44 = arg1 + 1687486377
    if arg2 < arg1:
        var45 = arg2 | var38
    else:
        var45 = var41 ^ var40 + (var41 + arg1)
    var46 = arg1 | var40 + var37 & -576
    var47 = var38 + -556
    var48 = (var46 | (var38 & arg1)) ^ arg2
    var49 = var46 - var46
    var50 = var37 ^ var47
    var51 = var49 - var48
    var52 = var50 - var36 & var44 ^ var51
    var53 = ((var41 | var42) - var37) + var46
    var54 = var6 - (var6 | var48) | var40
    if var6 < var54:
        var55 = var52 - var42 - var48 & var54
    else:
        var55 = var41 - var36 - var52
    if arg2 < var44:
        var56 = var47 | var50
    else:
        var56 = var46 ^ 507166362
    var57 = var53 - (var52 | var36)
    var58 = var37 - var48 & (var37 ^ var47)
    var59 = var6 + var46
    result = var58 ^ var36 + var57
    return result
def func12():
    func10()
    result = len(xrange(33))
    func11()
    return result
def func11():
    global len
    del len
def func10():
    global len
    len = lambda x : -9
class class8(object):
    def func9(self, arg10, arg11):
        return 0
def func7():
    func5()
    result = len(range(20))
    func6()
    return result
def func6():
    global len
    del len
def func5():
    global len
    len = lambda x : -7
def func2(arg3, arg4):
    closure = [0]
    def func3(acc, rest):
        var5 = -8 + 5 ^ -2 - -8 & acc ^ closure[0] | acc
        closure[0] += var5
        if acc == 0:
            return var5
        else:
            result = func3(acc - 1, var5)
            return result
    result = func3(10, 0)
    return result
if __name__ == "__main__":
    print 'prog_size: 5'
    print 'func_number: 13'
    print 'arg_number: 60'
    for i in xrange(25000):
        x = 5
        x = func1(x, i)
        print x,
