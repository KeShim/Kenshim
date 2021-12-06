export_file_path = '' #ファイルの出力先
import_folder_path = ''#ファイルパスを作成

path = import_folder_path + '/' + '*.xlsx'
file_path = glob.glob(path)#globは特定の条件に該当するファイルを取得できる
file_path

df_concat = pd.DataFrame()

for i in file_path:
    df_read_excel = pd.read_excel(i)
    df_concat = pd.concat([df_read_excel, df_concat])
    df_concat

    df_drop = df_concat.drop('Unnamed: 0', axis = 1)
    df_drop.head(3)
    df_sort = df_drop.sort_values(by = '達成率', ascending = False) # 達成率順に並び替え
    df_sort
    df_sort.to_excel(export_file_path + '/' + '保存したいファイル名.xlsx')

    workbook = openpyxl.load_workbook(export_file_path + '/保存したいファイル名.xlsx')
    worksheet = workbook.worksheet[0]
    worksheet.delete_cols(1)
    workbook.sava(export_file_path + '保存したいファイル名_01.xlsx')
