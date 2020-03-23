"""
输入某门课程成绩，将其转换成五级制（优、良、中、及格、不及格）
的评定等级

"""
score = int(input('请输入成绩：'))

if score < 60:
    print('不及格')
elif score < 70:
    print('及格')
elif score < 80:
    print('中等')
elif score < 90:
    print('良好')
else:
    print('优秀')