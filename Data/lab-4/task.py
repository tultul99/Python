import pandas as pd
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression

# Read the dataset
df = pd.read_csv('D:\Code\Python\VS Code\Data\lab-4\Ecommerce.csv')

# Check the head of the dataset, and check out its info() and describe() methods
print(df.head())
print(df.info())
print(df.describe())

# Explore the types of relationships across the entire dataset with pairplot
sns.pairplot(df)

# Split the dataset into training and testing data
X = df.drop('Time on App', axis=1) #replace target_variable with your target variable name
y = df['Time on Website'] #replace target_variable with your target variable name
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=101)

# Train the model
logmodel = LogisticRegression()
logmodel.fit(X_train,y_train)

# Predict the test data
predictions = logmodel.predict(X_test)
