from zenml import pipeline
from steps.ingest_data import ingest_df
from steps.clean_data import clean_data
from steps.model_train import train_model
from steps.evaluation import evaluation

from steps.config import ModelNameConfig


@pipeline(enable_cache = True)
def train_pipeline(data_path: str):
    df = ingest_df(data_path)
    X_train, X_test, y_train, y_test = clean_data(df)
    config = ModelNameConfig(model_name="LinearRegression")  # or the desired model name
    model = train_model(X_train, X_test, y_train, y_test, config)
    r2_score, rmse = evaluation(model, X_test, y_test)
