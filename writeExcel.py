from os.path import join
from time import strftime
import xlrd
import xlwt
from xlutils.copy import copy

excel_path = r"D:\selenium抓取的数据"  # 写入的excel文件路径
# now_time = strftime("%Y-%m-%d-%H")  # 获取时间戳为excel文件名和表名


# 创建excel追加数据到表中
class Write_Excel():
    def __init__(self):
        self.path = excel_path
        self.name = "笔趣阁数据预计十二万条（标题）3.xls"
        self.filename = join(self.path, self.name)

    # 设置表格样式
    def set_style(self, name, height, bold=False):
        style = xlwt.XFStyle()
        font = xlwt.Font()
        font.name = name
        font.bold = bold
        font.color_index = 4
        font.height = height
        style.font = font
        return style

    # 新建excel文件
    def new_excel(self):
        f = xlwt.Workbook()
        f.add_sheet('笔趣阁2', cell_overwrite_ok=True)  # 新增excel中表now_time
        f.save(self.filename)
        print("文件【%s】创建成功" % self.name)

    # 对excel文件写入数据
    def add_to_excel(self, values):
        try:
            workbook = xlrd.open_workbook(self.filename)  # excel文件存在则直接打开
        except FileNotFoundError:  # excel文件不存在则先创建在打开
            self.new_excel()
            workbook = xlrd.open_workbook(self.filename)
        sheets = workbook.sheet_names()  # 获取工作簿中的所有表格
        worksheet = workbook.sheet_by_name(sheets[0])  # 获取工作簿中所有表格中的的第一个表格
        rows_old = worksheet.nrows  # 获取表格中已存在的数据的行数
        if rows_old == 0:  # 跳过首行写入,留存为标题行
            rows_old = 1
        new_workbook = copy(workbook)  # 将xlrd对象拷贝转化为xlwt对象,旧数据复制保存
        new_worksheet = new_workbook.get_sheet(0)  # 获取转化后工作簿中的第一个表格
        i = 0
        for value in values:
            new_worksheet.write(rows_old, i, value)  # 追加写入数据,从rows_old列？开始写入
            i += 1
        print(" 文件【{0}】表【{1}】第【{2}】行追加数据{3}".format(self.name, '笔趣阁2', rows_old, values))
        # 定义标题行信息
        title_row = ["类别", "书名", "作者", "最新章节", "总字数", "更新日期"]
        for n in range(0, len(title_row)):
            new_worksheet.write(0, n, title_row[n], self.set_style('Times New Roman', 220, True))
        new_workbook.save(self.filename)  # 保存excel文件


if __name__ == "__main__":
    values_1 = [1, "百度搜索", "百度-百度搜索", "https://www.baidu.com", "Selenium"]
    values_2 = [2, "百度搜索", "百度-百度搜索", "https://www.baidu.com", "Python"]
    Write_Excel().add_to_excel(values=values_1)
    Write_Excel().add_to_excel(values=values_2)