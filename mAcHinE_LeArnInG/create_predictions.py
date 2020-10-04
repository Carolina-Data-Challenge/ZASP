from mAcHinE_LeArnInG.multi_layer_perceptron_regressor_model import MLPRegressorModel
import pandas as pd 

MLP_regressor_model = MLPRegressorModel(debug=False, data_depth=2, prediction_depth=3)
X, y, combined_data, county_codes = MLP_regressor_model.fetch_data()
model = MLP_regressor_model.train_and_test(X, y)
predictions = MLP_regressor_model.predict(combined_data, model)

#print(predictions)

## Save predictions 

predictions_df = pd.DataFrame(columns=['county_code','zasp_index','Year'])
for i in range(len(predictions)):
    for j in range(0,3):
        predictions_df.append({'county_code':county_codes[i],'zasp_index':predictions[i][j],'Year': (2020+j)},ignore_index=True)
        
predictions_df['zasp_index'] = predictions_df['zasp_index'].transform(lambda x: min(x, 100))
predictions_df.to_csv("predictions.csv",index = False)
# TODO Predictions might produce values higher than 100...
