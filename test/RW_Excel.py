import xlwt
from common import random_email, random_name, random_id, random_phone, random_username

import time


# 设置表格样式

def set_style(name, height, bold=False):
    style = xlwt.XFStyle()

    font = xlwt.Font()

    font.name = name

    font.bold = bold

    font.color_index = 4

    font.height = height

    style.font = font

    return style


# 写Excel

def write_excel():
    f = xlwt.Workbook()

    sheet1 = f.add_sheet('导入', cell_overwrite_ok=True)

    row0 = ["员工姓名", "员工工号", "手机号", "邮箱", '身份证号', '登录账号', '登录密码', '组织编号', '岗位编号', '上级工号']

    # default = easyxf(set_style('Times New Roman', 220, True))
    # 写第一行
    # for i in range(0, len(row0)):
    #     sheet1.write(0, i, row0[i], set_style('Times New Roman', 220, True))
    for x in range(1, 3):
        # random_name.random_name()-随机姓名
        # random_phone.create_phone()-随机电话号
        # random_email.RandomEmail()-随机邮箱
        # random_id.IDcard()-随机身份证
        # random_username.get_userNameAndPassword()-随机账号、密码
        row1 = [random_name.random_name(), "", random_phone.create_phone(), random_email.RandomEmail(),
                random_id.IDcard(),
                random_username.get_userNameAndPassword(), '11', 'R01Z066',
                'P0112', '00001']
        for i in range(0, len(row0)):
            # '''第一行'''
            sheet1.write(0, i, row0[i])
            # 其他行
            sheet1.write(x, i, row1[i])

        # 写第一列

        # for i in range(0, len(colum0)):
        #     sheet1.write(i + 1, 0, colum0[i], set_style('Times New Roman', 220, True))
        #
        #     sheet1.write(1, 3, '2006/12/12')
        #
        #     sheet1.write_merge(6, 6, 1, 3, '未知')  # 合并行单元格
        #
        #     sheet1.write_merge(1, 2, 3, 3, '打游戏')  # 合并列单元格
        #
        #     sheet1.write_merge(4, 5, 3, 3, '打篮球')

        f.save('/Users/wang/Downloads/pic/员工信息1.xlsx')


if __name__ == '__main__':
    # for i in range(1,10):
    #    print( random_username.get_userNameAndPassword(),'导入')
    print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
    write_excel()
