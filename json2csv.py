import json
import pandas as pd
import numpy as np
import glob
import sys
def main():
   fP = 0.5    #確度のデフォルト値
   #起動引数の処理
   args = sys.argv
   print(args)
   if len(args)<=1:
       #引数がないので終了
       sys.exit()
   if len(args)>1:
       strPath = sys.argv[1]
   if len(args)>2:
       fP = float(sys.argv[2])
   
   #フォルダ内のjsonファイルの一覧を作る
   json_list = glob.glob("outputs/" + strPath + "\*.json")
   ilenlist = len(json_list)
   #各点の名前を指定 
   cols =['Nose_x','Nose_y','P0','Neck_x','Neck_y','P1','RShoulder_x','RShoulder_y',
           'P2','RElbow_x','RElbow_y','P3','RWrist_x','RWrist_y','P4','LShoulder_x',
           'LShoulder_y','P5','LElbow_x','LElbow_y','P6','LWrist_x','LWrist_y','P7',
           'MidHip_x','MidHip_y','P8','RHip_x','RHip_y','P9','RKnee_x','RKnee_y',
           'P10','RAnkle_x','RAnkle_y','P11','LHip_x','LHip_y','P12','LKnee_x',
           'LKnee_y','P13','LAnkle_x','LAnkle_y','P14','REye_x','REye_y','P15',
           'LEye_x','LEye_y','P16','REar_x','REar_y','P17','LEar_x','LEar_y','P18',
           'LBigToe_x','LBigToe_y','P19','LSmallToe_x','LSmallToe_y','P20','LHeel_x',
           'LHeel_y','P21','RBigToe_x','RBigToe_y','P22','RSmallToe_x','RSmallToe_y',
           'P23','RHeel_x','RHeel_y','P24']
   dfsum = pd.DataFrame(index=[],columns=cols)
   #jsonファイルを読み込んで結合する
   for  i,file in enumerate(json_list):
       with open(file) as f:
           print(file)
           data = json.load(f)
           data = np.array(data['people'][0]['pose_keypoints_2d']).reshape(-1,75)
           # 3成分(X,Y,P)×25マーカ\
       df = pd.DataFrame(data,columns=cols)
       
       #「確度」の値によって、XYの値をNULLにする
       for num in range(2, 75, 3):
           if df.iat[0,num]<fP:
               df.iat[0,num-1]=np.nan
               df.iat[0,num-2]=np.nan
       #結合
       dfsum = dfsum.append(df, ignore_index=True)
       #進捗バー
       dPercent = (i+1)/ilenlist*100
       print("\r{0}% [{1}]".format(int(dPercent), "#" * int(dPercent)), end="")
   #出力する
   dfsum.to_csv('csv/' + strPath + '.csv')
if __name__ == '__main__':
   main()