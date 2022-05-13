# price-of-land-in-taipei
將政府公布之公告現值整理成shp，透過ArcGIS輸出於地圖，最後在寫入WebGIS。

# Step1 整理政府之開放資料
至政府之opendata下載開放資料(.csv) (https://data.gov.tw/en/datasets/122058)
並將其整理成可分析之資料：
如：臺北市	 松山區	西松段一小段	30000
應修改為：台北市松山區西松段一小段3號
使用Excel之concat函數，然後大地號求商；小地號求餘數，
最後將地址與公告地價、公告現值匯出成csv。

(Step 1 收錄Price.csv)

# Step2 讓python幫我們批量處理
將地址輸入API (https://twland.ronny.tw/) 然後透過多筆地號的服務 (如：https://twland.ronny.tw//index/search?lands[]=臺北市,華興段三小段,141&lands[]=臺北市,華興段三小段,142) 去批次處理。
而一個JSON檔只接受50筆地號，但整個台北市有42萬筆。
為了實現批量處理，可以透過Python的For迴圈去達到我們迭代的目的。
再者，為了後續的合併作業方便進行，將每200個抓下來的JSON檔組成一個資料夾，因為有41萬筆地號，
所以有41個資料價會被我們存於目錄當中

(Step 2 收錄PYTHON檔案及產出之資料)

# Step3 ArcGIS Pro 的 ModelBuilder 將json轉成shp
用ArcGISpro的ModelBuilder去幫助我們建立自己的地理處理工具(Geoprrocessing)，主要透過迭代器(Iterator)，將資料夾內的檔案迭代處理，處理方式為Json轉為圖徵(Features)，最後再將產出之成果收集(CollectValue)如圖：
<img width="586" alt="image" src="https://user-images.githubusercontent.com/101982224/167857521-961bf9d0-97c9-415a-8de8-5ec1f266ae09.png">

因為ModelBuilder不支援巢狀迭代，因此，我們新建一個Model將上一個Model所產出之200個圖徵聚合(Merge)再一起。
<img width="203" alt="image" src="https://user-images.githubusercontent.com/101982224/167858490-89afe40f-dc0e-409b-b95a-5bd9284eb3a9.png">

最後，再對這個Model按右鍵，點選Batch，選擇41個資料夾，然後等待結果。
<img width="518" alt="image" src="https://user-images.githubusercontent.com/101982224/167858460-4b38528c-4d23-4df9-8950-6c47034bc9e4.png">

(Step 3 收錄ModelBuilder的Python碼 及Output之資料)

# Step4 產生地號shp
將地理處理之成果聚合成一個大的shp，最後再與Step1之屬性表產生連結(Join)，如此一來，就有一個有公告現值及公告地價的shp了。

(Step 4 收錄該shp。)

# Step5 將此shp呈現於電子地圖。

(目前卡關)
