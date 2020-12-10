# Prediction of Patient’s Treatment Category
Hospitals are pretty busy nowadays. Doctors are carrying a lot of responsibilities.

Let's think of a doctor, whose patient came to have some examination or to have some one-day quick surgery. Such a patient shouldn't necessarily stay at the hospital overnight.
The decision whether to leave the hospital or to stay often can be tricky to make. 

This kind of a decision is usually based on multiple different factors, ranging from general health of the patient objective test results and some third circumstances,
like the amount of free space at the hospital and business of the personnel, for example during the coronavirus pandemic.
Therefore, this case present problems on different levels.


My project is trying solve this problem. 

# Approach

- **The dataset**: results if a complete blood cell count (CBC) test of a nearly 4.5K patients from one private hosplital. Target variable - patients' treatment category:
  - inpatient
  - outpatient
  
*Data source: Sadikin, Mujiono (2020), “EHR Dataset for Patient Treatment Classification”, Mendeley Data, V1, doi: 10.17632/7kv3rctx7m.1*
- **Training a classification ML model**. Starting from simple Logistic Regression model to MLP Classifier, the performance of the model was relatively not so high and remained the same.
The conclusion was that models, based on Decision Trees work the best in the case, particularly **Random Forest Classifier**.

- **Data preprocessing**. The data was already perfectly clean, and Decision Tree models usually do not require any specific data preprocessing.
However, was decided to apply the SMOTE technique to make the number of cases in each group more equal. Before SMOTE, Standars Scaler was applied.

- **Improving model performance**. The main goal was to train the model to accurately predict the inpatient category and to reduce the false negative predictions, 
so that in the real world there was a low risk of sending home a patient which requires supervision.Steps taken to achieve this:
  - Hyperparamether tuning
  - Class weights were given to make a model to better predict the inpatient category
  
# Results

The error metrics of a final model are:

  - The Accuracy(with cross-validation on 10 folds): 0.76 +- 0.1
  - The Kappa score: 0.56
  - The Recall for inpatient category: 0.81, for outpatient category: 0.74
  
# Conclusions

The ML model can predict the patient treatment category, but the precision is still not very high. This may be both because of the size of the training data,
and the fact that the dimensions are not sufficient for the model to learn to predict patient's category from retrospective data, because CBC is a very general type of test.

Therefore, the model improvement may be achieved with additional training examples and additional, more specific, input features.

Further research is warranted to assess potential performance improvements and clinical efficacy in a prospective trial.

# Presentation of a functionality

The classificcation model was wrapped in Flask application with UI, where the doctor or a nurse can type the patient's age and CBC result, and get a recommendation to either let the patient go home for a night, or to hospitalize him for further supervision.

The link to the PowerPoint presentation: https://drive.google.com/file/d/1pOWxd5TPCQriBe17N94aJ04T8NBtGiH8/view?usp=sharing
