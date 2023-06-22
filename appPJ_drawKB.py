import matplotlib.pyplot as plt
import matplotlib.patches as patches
import os



# 和弦指法
chord = {'C':[[4, 6, 8], []],
         'D':[[5, 9], [8]],
         'E':[[6, 10], [9]],
         'F':[[4, 7, 9], []],
         'G':[[5, 8, 10], []],
         'A':[[6, 9], [5]],
         'B':[[10], [6, 8]],
         
         'Cm':[[4, 8], [6]],
         'Dm':[[5, 7, 9], []],
         'Em':[[6, 8, 10], []],
         'Fm':[[4, 7], [9]],
         'Gm':[[5, 8], [10]],
         'Am':[[4, 6, 9], []],
         'Bm':[[5, 10], [8]],
         
         'C7':[[4, 6, 8], [10]],
         'D7':[[4, 5, 9], [8]],
         'E7':[[5, 6, 10], [9]],
         'F7':[[4, 7, 9], [6]],
         'G7':[[5, 7, 8, 10], []],
         'A7':[[6, 8, 9], [5]],
         'B7':[[9, 10], [6, 8]],
         
         'Cm7':[[4, 8], [6, 10]],
         'Dm7':[[4, 5, 7, 9], []],
         'Em7':[[5, 6, 8, 10], []],
         'Fm7':[[4, 7], [6, 9]],
         'Gm7':[[5, 7, 8], [10]],
         'Am7':[[4, 6, 8, 9], []],
         'Bm7':[[5, 9, 10], [8]],
         
         'CM7':[[4, 6, 8, 10], []],
         'DM7':[[5, 9], [5, 8]],
         'EM7':[[6, 10], [6, 9]],
         'FM7':[[4, 6, 7, 9], []],
         'GM7':[[5, 8, 10], [8]],
         'AM7':[[6, 9], [5, 9]],
         'BM7':[[10], [6, 8, 10]],
         
         }



# 輸入歌曲和弦用陣列儲存，然後畫出來
song_chord = input("song_chord：")
song_chord = song_chord.split(' ')
#print(song_chord)



# 依照歌曲和弦(song_chord 陣列)按照順序儲存每個和弦的按法
for chord_num in range(len(song_chord)):
    
    # 設定視窗大小和圖像大小
    fig, ax = plt.subplots(figsize=(5, 2))
    #ax = plt.subplots(figsize=(5, 2))
    
    # x, y 軸大小
    ax.set_xlim(0, 14.04)
    ax.set_ylim(0, 1.01)
    
    # 關掉軸
    plt.axis('off')
    
    
    
    # 繪製鋼琴鍵盤上的白鍵
    for i in range(14):
        rect = patches.Rectangle((i, 0.01), 1, 1, linewidth=1, edgecolor='black', facecolor='white')
        ax.add_patch(rect)
    
    for i in chord.get(song_chord[chord_num])[0]:
        rect = patches.Rectangle((i, 0.01), 1, 1, linewidth=1, edgecolor='black', facecolor='#7FB3E5')
        ax.add_patch(rect)    
      
    # 繪製鋼琴鍵盤上的黑鍵
    for i in [1, 2, 3, 5, 6, 8, 9, 10, 12, 13]:
        rect = patches.Rectangle((i - 0.3, 0.3), 0.6, 0.7, linewidth=1, edgecolor='black', facecolor='black')
        ax.add_patch(rect)
    
    for i in chord.get(song_chord[chord_num])[1]:
        rect = patches.Rectangle((i - 0.3, 0.3), 0.6, 0.7, linewidth=1, edgecolor='black', facecolor='#7FB3E5')
        ax.add_patch(rect)
    
    # 儲存圖形到放和弦的資料夾
    output_directory = 'D:/appPJ/SongsChordGraph'
    #file_path = os.path.join(output_directory, f"song_chord {chord_num}.png")
    lower = song_chord[chord_num].lower()
    file_path = os.path.join(output_directory, "chord_" + str(lower) + ".png")
    plt.savefig(file_path, bbox_inches="tight")
        
    # 清除當前的圖形
    ax.clear()



print('Finish')

