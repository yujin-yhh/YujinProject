# 加法测试用例
def test_add(getadddata, getcal, comm_func):
    # adddata = getdata
    assert getadddata[2] == getcal.add(getadddata[0], getadddata[1])


# 减法测试用例
def test_sub(getsubdata, getcal, comm_func):
    subdata = getsubdata
    assert getsubdata[2] == getcal.sub(getsubdata[0], getsubdata[1])


# 除法测试用例
def test_div(getdivdata, getcal, comm_func):
    assert getdivdata[2] == getcal.div(getdivdata[0], getdivdata[1])


# 乘法测试用例
def test_mul(getmuldata, getcal, comm_func):
    # 添加断言
    assert getmuldata[2] == getcal.mul(getmuldata[0], getmuldata[1])



