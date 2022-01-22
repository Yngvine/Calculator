# This is a sample Python script.
import PyQt5.QtWidgets as qtw
# Press Mayús+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


class MainWindow(qtw.QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Chapato')
        self.setLayout(qtw.QVBoxLayout())
        self.keypad()
        self.temp_num = []
        self.op_num = []
        self.error_buff = ''

        self.show()

    def keypad(self):
        container = qtw.QWidget()
        container.setLayout(qtw.QGridLayout())

        self.calc_field = qtw.QLineEdit()
        b_result = qtw.QPushButton('=', clicked = self.func_result)
        b_clear = qtw.QPushButton('AC', clicked = self.clear_calc)
        b_del = qtw.QPushButton('DEL', clicked=self.del_element)
        b_1 = qtw.QPushButton('1', clicked = lambda: self.num_press('1'))
        b_2 = qtw.QPushButton('2', clicked = lambda: self.num_press('2'))
        b_3 = qtw.QPushButton('3', clicked = lambda: self.num_press('3'))
        b_4 = qtw.QPushButton('4', clicked = lambda: self.num_press('4'))
        b_5 = qtw.QPushButton('5', clicked = lambda: self.num_press('5'))
        b_6 = qtw.QPushButton('6', clicked = lambda: self.num_press('6'))
        b_7 = qtw.QPushButton('7', clicked = lambda: self.num_press('7'))
        b_8 = qtw.QPushButton('8', clicked = lambda: self.num_press('8'))
        b_9 = qtw.QPushButton('9', clicked = lambda: self.num_press('9'))
        b_0 = qtw.QPushButton('0', clicked = lambda: self.num_press('0'))
        b_plus = qtw.QPushButton('+', clicked = lambda: self.func_press('+'))
        b_minus = qtw.QPushButton('-', clicked = lambda: self.func_press('-'))
        b_mul = qtw.QPushButton('x', clicked = lambda: self.func_press('*'))
        b_div = qtw.QPushButton('%', clicked = lambda: self.func_press('/'))

        container.layout().addWidget(self.calc_field,0,0,1,4)
        container.layout().addWidget(b_del, 1, 0, 1, 2)
        container.layout().addWidget(b_clear, 1, 2, 1, 2)
        container.layout().addWidget(b_1, 2, 0)
        container.layout().addWidget(b_2, 2, 1)
        container.layout().addWidget(b_3, 2, 2)
        container.layout().addWidget(b_plus, 2, 3)
        container.layout().addWidget(b_4, 3, 0)
        container.layout().addWidget(b_5, 3, 1)
        container.layout().addWidget(b_6, 3, 2)
        container.layout().addWidget(b_minus, 3, 3)
        container.layout().addWidget(b_7, 4, 0)
        container.layout().addWidget(b_8, 4, 1)
        container.layout().addWidget(b_9, 4, 2)
        container.layout().addWidget(b_mul, 4, 3)
        container.layout().addWidget(b_0, 5, 0, 1, 2)
        container.layout().addWidget(b_result, 5, 2)
        container.layout().addWidget(b_div, 5, 3)

        self.layout().addWidget(container)

    def num_press(self, n):
        self.temp_num.append(n)
        temp_str = ''.join(self.temp_num)
        if self.op_num:
            self.calc_field.setText(''.join(self.op_num) + temp_str)
        else:
            self.calc_field.setText(temp_str)

    def func_press(self, o):
        temp_str = ''.join(self.temp_num)
        self.op_num.append(temp_str)
        self.op_num.append(o)
        self.temp_num = []
        self.calc_field.setText(''.join(self.op_num))

    def func_result(self):
        fin_str = ''.join(self.op_num) + ''.join(self.temp_num)
        try:
            res_str = eval(fin_str)
            fin_str += '='
            fin_str += str(res_str)
            self.calc_field.setText(fin_str)
        except ArithmeticError as ar:
            self.error_buff = self.calc_field.text()
            self.calc_field.setText('error:' + ar.__str__())
        except ValueError as v:
            self.error_buff = self.calc_field.text()
            self.calc_field.setText('error:' + v.__str__())
        except Exception as e:
            self.error_buff = self.calc_field.text()
            self.calc_field.setText('error:' + e.__str__())


    def clear_calc(self):
        self.calc_field.clear()
        self.temp_num = []
        self.op_num = []

    def del_element(self):
        if '=' in self.calc_field.text():
            pos = self.calc_field.text().rfind('=')
            self.calc_field.setText(self.calc_field.text()[:pos])
        elif 'e' in self.calc_field.text():
            self.calc_field.clear()
            self.calc_field.setText(self.error_buff)
            self.error_buff = ''
        elif self.calc_field.text():
            self.calc_field.setText(self.calc_field.text()[:-1])
            if self.temp_num:
                self.temp_num = self.temp_num[:-1]
            else:
                self.op_num = self.op_num[:-1]




def main():
    app = qtw.QApplication([])
    mw = MainWindow()
    app.exec_()

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()





# See PyCharm help at https://www.jetbrains.com/help/pycharm/
