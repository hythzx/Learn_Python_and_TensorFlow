#dic/dict
#key-value:键-值


dFriend = {
    "name":"sanduo",
    "age":18,
    "isMale":True,
    1:1
    #1:1    key具有唯一性
}

print(dFriend["name"])
print(dFriend.get("name"))
print(dFriend.get(1))
print(dFriend["isMale"])
dFriend["isMale"] = False
print(dFriend["isMale"])

"""
Python字典包含了以下内置函数：

1   cmp(dict1, dict2)   比较两个字典元素。
2   len(dict)           计算字典元素个数，即键的总数。
3   str(dict)           输出字典可打印的字符串表示。
4   type(variable)      返回输入的变量类型，如果变量是字典就返回字典类型。

Python字典包含了以下内置方法：

1	dict.clear()                删除字典内所有元素
2	dict.copy()                 返回一个字典的浅复制
3	dict.fromkeys(seq[, val])   创建一个新字典，以序列 seq 中元素做字典的键，val 为字典所有键对应的初始值
4	dict.get(key, default=None) 返回指定键的值，如果值不在字典中返回default值
5	dict.has_key(key)           如果键在字典dict里返回true，否则返回false
6	dict.items()                以列表返回可遍历的(键, 值) 元组数组
7	dict.keys()                 以列表返回一个字典所有的键
8	dict.setdefault(key, default=None)  和get()类似, 但如果键不存在于字典中，将会添加键并将值设为default
9	dict.update(dict2)          把字典dict2的键/值对更新到dict里
10	dict.values()               以列表返回字典中的所有值
11	pop(key[,default])          删除字典给定键 key 所对应的值，返回值为被删除的值。
                                key值必须给出。 否则，返回default值。
12	popitem()                   返回并删除字典中的最后一对键和值。
"""