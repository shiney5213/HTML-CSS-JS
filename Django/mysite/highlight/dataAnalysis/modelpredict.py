from tensorflow.keras.models import load_model
from sklearn.preprocessing import MinMaxScaler
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def modelpre( args, ddf,):
    # 모델 경로
    filename = args['filename']
    data_path = args['data_root']
    model = load_model('./static/highlight/highlight_3.h5')
    print(model)
    # 인풋값 경로
    # df = pd.read_excel('/content/drive/My Drive/highlight/송호성의 방/hl/20200506_Faker_612874923.mp4_5.xlsx')
    df = ddf
    print('df', len(df))
    # del df['Unnamed: 0']
    timeidx = df['time']
    df.set_index('time', inplace=True)

    scaler = MinMaxScaler()
    scale_cols = ['k','d','a','gold','ha','sa','an','ca','dis','fe','sup','conf','sound']
    df_scaled = scaler.fit_transform(df[scale_cols])

    df_scaled = pd.DataFrame(df_scaled)
    df_scaled.columns = scale_cols

    def make_dataset2(data, window_size=20):
        feature_list = []
        # label_list = []
        for i in range(len(data) - window_size):
            feature_list.append(np.array(data.iloc[i:i+window_size]))
            # label_list.append(np.array(label.iloc[i+window_size]))
        # return np.array(feature_list), np.array(label_list)
        return np.array(feature_list)

    feature_cols = ['k','d','a','gold','ha','sa','an','ca','dis','fe','sup','conf','sound']
    # label_cols = ['count']

    test = df_scaled

    test_feature = test[feature_cols]
    # test_label = test[label_cols]

    # test dataset (실제 예측 해볼 데이터)
    test_feature = make_dataset2(test_feature, 20)
    # print(test_feature.shape, test_label.shape)
    # ((180, 20, 4), (180, 1))
    pre = model.predict(test_feature)
    pre = pd.DataFrame(pre)
    timeidx=timeidx[20:].reset_index()
    pre=pre.reset_index()
    timeidx=timeidx.reset_index()
    final = pd.merge(pre, timeidx, left_on='index', right_on='level_0')
    final = final[['time', 0]]
    final.rename(columns={0:"probability"}, inplace = True)

    save_dir = filename.replace('mp4', '')
    
    final.to_csv(data_path + '/final.csv', index = False)

    pltx = 900/72
    plty = 144/72

    plt.rcParams['figure.figsize'] = (pltx,plty)
    plt.rcParams['lines.linewidth'] = 2
    plt.rcParams['lines.color']= 'r'
    plt.rcParams['axes.grid'] = True

    
    dataframe = final['probability']
    plt.plot(dataframe)
    plt.yticks([0,1])
    plt.draw()
    fig = plt.gcf()

    img_name = f'{data_path}/highlight.png'
    ('save', img_name)
    fig.savefig(img_name, dpi = fig.dpi,  bbox_inches='tight')
    return final