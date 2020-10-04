from mAcHinE_LeArnInG.multi_layer_perceptron_regressor_model import MLPRegressorModel

MLP_regressor_model = MLPRegressorModel(debug=True, data_depth=2, prediction_depth=5)
X, y, combined_data = MLP_regressor_model.fetch_data()
model = MLP_regressor_model.train_and_test(X, y)
predictions = MLP_regressor_model.predict(combined_data, model)

print(predictions)

# TODO Predictions might predict values higher than 100...
