# How to Grid Search ARIMA Model Hyperparameters with Python
https://machinelearningmastery.com/grid-search-arima-hyperparameters-with-python/


## ARIMAモデルの評価
``evaluate_arima_model関数``  
引数 : X : データセット,arima_order : タプル[p,q,d]

1. データセットを学習セットとテストセットに分割する(学習セット:テストセット=66:36).
2. 学習セットを訓練セットと評価セットに分割する.
3. ARIMAモデルを訓練する.
4. one-stepの予測を行う.
5. 予測値と実測値を比較して誤差を計算する.

後は,パラメータp,q,dのグリッドを指定してevaluate_arima_model関数で
評価させればよい.