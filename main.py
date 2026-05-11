import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error
from xgboost import XGBRegressor

# Load data
train_data = pd.read_csv("data/train.csv")
test_data = pd.read_csv("data/test.csv")

# Select numeric columns only
numeric_cols = train_data.select_dtypes(include=['int64', 'float64']).columns

# Remove target from features
features = [col for col in numeric_cols if col != "SalePrice"]

# Fill missing values
X = train_data[features].fillna(0)
y = train_data["SalePrice"]

X_test = test_data[features].fillna(0)

# Split data
X_train, X_valid, y_train, y_valid = train_test_split(
    X, y, test_size=0.2, random_state=1
)

# Model
model = XGBRegressor(
    n_estimators=1000,
    learning_rate=0.05,
    random_state=1
)

# Train
model.fit(X_train, y_train)

# Validation predictions
preds = model.predict(X_valid)

# Score
mae = mean_absolute_error(y_valid, preds)

print("MAE:", mae)

# Train on full data
model.fit(X, y)

# Predict test set
test_preds = model.predict(X_test)

# Submission file
output = pd.DataFrame({
    "Id": test_data.Id,
    "SalePrice": test_preds
})

output.to_csv("submission.csv", index=False)

print("New submission file created!")