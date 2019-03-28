from scipy.fftpack import fft

words = ['数字', '语音', '语言', '识别', '中国',
         '总工', '北京', '背景', '上海', '商行',
         '复旦', '饭店', 'Speech', 'Speaker', 'Signal',
         'Process', 'Print', 'Open', 'Close', 'Project']

repeat = 20

stdno = 1630713
for i in range(len(words)):
    for j in range(repeat):
        filename = "%s-%02d-%02d" % (stdno, i, j + 1)
        # print(filename)

