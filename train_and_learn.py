import joblib
from sklearn.metrics import mean_absolute_error, r2_score
from catboost import CatBoostRegressor
from sklearn.model_selection import train_test_split
import numpy as np
import pandas as pd

df = pd.read_csv("property_maintenance_records.csv")

# categorical_features = ['component', 'job_scope']


X = df[['component', 'job_scope', 'component_age_years',
        'inspection_score', 'contractor_hours']]
y = df['repair_cost']

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)


model = CatBoostRegressor(
    iterations=500,
    learning_rate=0.05,
    depth=8,
    loss_function='MAE',
    verbose=False
)

model.fit(
    X_train, y_train,
    cat_features=[0, 1]  # component, job_scope
)

single_request = pd.DataFrame([{
    'component': 'washing_machine',
    'job_scope': 'moderate',
    'component_age_years': 17,
    'inspection_score': 49,
    'contractor_hours': 1.5
}])

# prediction = model.predict(single_request)
# print("Actual repair cost was:", 87)
# print("Predicted repair cost:", prediction[0])


preds = model.predict(X_test)

print("MAE:", mean_absolute_error(y_test, preds))
print("R2:", r2_score(y_test, preds))

joblib.dump(model, "model.pkl")
