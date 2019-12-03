def ssd1306_i2c_lump_print_str(oled, text, x_size, y_size, x_axis, y_axis):
    max_row = y_size // 16
    max_col = x_size // 8
    x_axis = x_axis // 8
    y_axis = y_axis // 16
    row = 0
    col = 0
    for i in text:
        is_cn = i.encode('utf-8')
        if col == max_col:
            col = 0
            row += 1
            if row == max_row:
                break
        else:
            if len(is_cn) >= 2:
                if col == max_col - 1:
                    row += 1
                    col = 0
                    oled.draw_chinese(i, col + x_axis, row + y_axis)
                    col += 2
                else:
                    oled.draw_chinese(i, col + x_axis, row + y_axis)
                    col += 2
            else:
                oled.draw_chinese(i, col + x_axis, row + y_axis)
                col += 1
