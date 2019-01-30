"""
    拼接sql
"""
import csv



def main():
    """
        主函数
    """

    with open('321.csv', 'rt', encoding="utf-8") as f:

        reader = csv.reader(f)
        for row in reader:
            sql_str = 'sql'
            sql_str += row[0] + ",'"
            sql_str += row[1] + "',"
            if row[2] == 'NULL':
                sql_str += row[2] + ","
            else:
                sql_str += "'" + row[2] + "',"
            sql_str += row[3] + ","
            sql_str += row[4] + ","
            sql_str += row[5] + ",'"
            sql_str += row[6] + "',"
            sql_str += "getDate(),'"
            sql_str += row[8] + "','"
            sql_str += row[9] + "',"
            sql_str += row[10] + ","
            sql_str += row[11] + ",'"
            sql_str += row[12] + "',"
            sql_str += row[13] + ","
            sql_str += row[14] + ","
            sql_str += row[15] + ","
            sql_str += row[16] + ","
            sql_str += row[17] + ","
            sql_str += row[18] + ","
            sql_str += row[19] + ","
            sql_str += row[20] + ","
            sql_str += row[21] + ","
            sql_str += row[22] + ","
            if row[23] == 'NULL':
                sql_str += row[23] + ","
            else:
                sql_str += "'" + row[23] + "',"
            sql_str += row[24] + ","
            sql_str += row[25] + ",'"
            sql_str += row[26] + "','"
            sql_str += row[27] + "',"
            sql_str += row[28] + ","
            if row[29] == 'NULL':
                sql_str += row[29] + ","
            else:
                sql_str += "'" + row[29] + "',"
            if row[30] == 'NULL':
                sql_str += row[30] + ","
            else:
                sql_str += "'" + row[30] + "',"
            if row[31] == 'NULL':
                sql_str += row[31] + ",'"
            else:
                sql_str += "'" + row[31] + "','"
            sql_str += row[32] + "',"
            if row[33] == 'NULL':
                sql_str += row[33] + ""
            else:
                sql_str += "'" + row[33] + "'"
            sql_str += ");"




            print(sql_str)


if __name__ == '__main__':
    main()