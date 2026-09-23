from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import make_column_selector as selector
from sklearn.ensemble import RandomForestClassifier

PATH="learning_set/WA_Fn-UseC_-Telco-Customer-Churn.csv"
URL = "http://api:8000/predict_churn"

#uzupelniamy brakujaca liczbe mediana
NUMERIC_TRANSFORMER = SimpleImputer(strategy='median')

#uzupelniamy braki najczestsza wartoscia, chronimy rowniez przed nowa dana ktora wpisal uzytkownik a nie wiemy co to jest
CATEGORICAL_TRANSFORMER = Pipeline(steps=[
    ('imputer', SimpleImputer(strategy='most_frequent')),
    ('encoder', OneHotEncoder(handle_unknown='ignore'))
])

PREPROCESSOR = ColumnTransformer(
    transformers=[
        ('num', NUMERIC_TRANSFORMER, selector(dtype_exclude="object")),
        ('cat', CATEGORICAL_TRANSFORMER, selector(dtype_include="object"))
    ])

CHURN_MODEL_PIPELINE = Pipeline(steps=[
    ('preprocessor', PREPROCESSOR),
    ('classifier', RandomForestClassifier(n_estimators=100, random_state=42, class_weight='balanced', max_depth=10))
])

MODEL= "model/model.joblib"
COLUMNS_TYPES="columns/columns_types.joblib"