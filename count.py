# coding:utf8
import re
from os import listdir

path42 = '4.2'
path4 = '4.0'
pattern_element='(?<=<xs:element name=")\w+'
pattern_attribute='(?<=<xs:attribute name=")\w+'
pattern_complexType='(?<=<xs:complexType name=")\w+'
pattern_simpleType='(?<=<xs:simpleType name=")\w+'
pattern_group='(?<=<xs:group name=")\w+'
pattern_attributeGroup='(?<=<xs:attributeGroup name=")\w+'
def find_data(path,pattern):
    try:
       with open(path) as f:
            content = f.read()
            p_attr=re.compile(pattern)
            result = p_attr.findall(content)
            return sorted(result)
    except:
       pass
    return []
def main(pattern):
    files42 = [f for f in listdir(path42) if f.endswith('xsd')]
    print(len(files42))

    for f in  sorted(files42):
        print('----' + f + ' start-----')
        r42= find_data(path42+'/'+f,pattern)
        r4=find_data(path4+'/'+f,pattern)
        print('4.2数量:'+str(len(r42)))
        print(r42)
        print('4.0数量:'+str(len(r4)))
        print(r4)
        add= set(r42).difference(set(r4))
        print('增加:'+ str(len(add)))
        print(sorted(list(add)))
        remove=set(r4).difference(set(r42))
        print('删除:' + str(len(remove)))
        print(sorted(list(remove)))
        print('----'+f+' end-----')

if __name__=='__main__':
    print("元素开始")
    main(pattern_element)
    print("元素结束，属性开始")
    main(pattern_attribute)
    print("属性结束，复杂类型开始")
    main(pattern_complexType)
    print("复杂类型结束，简单类型开始")
    main(pattern_simpleType)
    print("简单类型结束，分组开始")
    main(pattern_group)
    print("分组结束，属性组开始")
    main(pattern_attributeGroup)
    print("属性组结束")

