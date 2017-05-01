<html>
  <body>
    <p>
      Hello World!<br>
      Today we are going to create a simple classification model by using a random forest classifier<br>
    </p>
    <p>
    We are gonna need the dataset for this tutorial. You can get it from
    <a href="https://www.kaggle.com/artimous/complete-fifa-2017-player-dataset-global" class="url">here</a>.<br>
    If you don't know it, Kaggle is an awesome website where you can find all sort of open datasets for datascience
    and you can also compete with other users to earn prizes.<br>
    The project folder will be like this:<br>
    <img class="alignnone size-full wp-image-404" src="/2017/05/cmd-path.png" alt="Folder Tree" width="155" height="117">
    </p>
    <!-- <p> -->
      Let's start coding!
      <pre>
        <code>from sklearn.ensemble import RandomForestClassifier
import pandas as pd
import numpy as np\n
\# Let's open the dataset
players = pd.read_csv("data/Fulldata.csv")</code>
      </pre>
      The first thing to do is to import pandas and numpy and to open the dataset
      as a pandas DataFrame. Don't worry if you have never used a dataframe before,
      we are going to take a look at how it works.
      <pre>
        <code>\# To check first 5 rows of the dataset
players.head()
\# To check some numeric informations about a column
players.loc[:,'Rating'].describe()
\# Get column names
list(players)
\# Selection by label
players.loc[:,['Name','Rating']]
\# Selection by index
players.iloc[:,[0,4]]</code>
      </pre>
      These are only a few of the many functions included in Pandas. I really suggest
      you to check <a href="http://pandas.pydata.org/pandas-docs/stable/10min.html" class="url">it</a> out.<br>
      Now we can go back to our program:
      <pre>
        <code>\# Add a column that tells us if it's Training Data or not
players['is_train'] = np.random.uniform(0, 1, len(players)) <= .75\n
\# Divide between training and testing data
train, test = players[players['is_train'] == True],players[players['is_train'] == False]\n
\# We choose the columns with player stats
features = players.columns[17:53]
\# Split into Training X(stats) and Y(rating) data
X = train[features]
Y = train.loc[:,'Rating']</code>
    </pre>
    In the first part of the code we add a column to tell us if it's train data or not
    by using a pandas function which creates a series of number with an uniform distribution.
    Then we divide our dataframe into train and test.<br>
    After this we need to choose which columns we are going to consider to train
    the model. We are going to use all the columns which contains player stats.<br>
    Then we split the training data into Features and Result.
    <pre>
      <code>\# Initialize the Classifier and train it
clf = RandomForestClassifier(n_jobs=4)
clf.fit(X, Y)\n
\# Get the predictions
preds = clf.predict(test[features])</code>
    </pre>
    We can now initialize the classifier and get the predictions.
    <pre>
      <code># Create an output dataframe
out = test.loc[:,['Name','Rating']]
out['prediction'] = preds
out['diff']=out.loc[:,'Rating']-out.loc[:,'prediction']
\# Let's print mean difference between predicted and actual
print('Mean difference: ',out['diff'].mean())
\# And the number of exact matches
print('Exact Matches:',len(out[out['diff']==0]))</code>
    </pre>
    With this last step we are going to create an output dataframe from test.
    Then we add the column prediction and diff(difference between predicted value and rating)
    and finally we print the mean difference and the number of exact matches.<br>
    Your output should be similar to this:
    <pre>
      <code>Mean difference:  0.5449783648371669
Exact Matches: 821</code>
    </pre>
    We can also check the content of the output dataframe.
    <pre>
      <code>\#Let's print the players with rating and prediction
print(out.loc[:,['Name','Rating','prediction','diff']])
\# OUTPUT
\#    Name                  Rating   prediction  diff
\#0    Cristiano Ronaldo      94          88     6
\#3          Luis Suárez      92          88     4
\#4         Manuel Neuer      92          81    11
\#8   Zlatan Ibrahimović      90          85     5
\#10      Jérôme Boateng      89          85     4
      </code>
    </pre>
    We can improve our score by using another algorithm, but i think it's enough
    for today. You can download the code of this post <a href="https://github.com/Inzaniak/pybistuff/tree/master/Fifa" class="url"> here</a><br>
    Have fun experimenting with other datasets!
    <!-- </p> -->
  </body>
</html>