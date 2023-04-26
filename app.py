import gzip
import pickle
import streamlit as st


with gzip.open('BinaryData.pkl.gz', 'rb') as f:
    model = pickle.load(f)

def predict(float_features):
    predicted_value = model.predict(float_features)
    if predicted_value[0] == 1:
        return "Fully paid"
    else:
        return "Not fully paid"
    
def main():
    st.set_page_config(page_title='identifying credit worthy borrowers ')
    st.title('Identifying credit worthy borrowers')
#     st.write("Please enter the required input parameters:")
    features = ['credit_policy', 'int_rate', 'installment', 'log_annual_inc', 'dti',
       'fico', 'days_with_cr_line', 'revol_bal', 'revol_util',
       'inq_last_6mths', 'delinq_2yrs', 'pub_rec', 'purpose_credit_card',
       'purpose_debt_consolidation', 'purpose_educational',
       'purpose_home_improvement', 'purpose_major_purchase',
       'purpose_small_business']
    float_features = []
    for feature in features:
        if feature == "credit_policy" or feature == "purpose_credit_card" or feature == "purpose_debt_consolidation" or feature == "purpose_educational" or feature == "purpose_home_improvement" or feature == "purpose_major_purchase" or feature == "purpose_small_business":
            value = st.radio(feature,[0,1])
            float_features.append(value)
        else:
            value = st.number_input(feature, min_value=0.0)
            float_features.append(value)
            
    if st.button('Predict'):
        result = predict([float_features])
        st.write('The credit status is:', result)

if __name__ == "__main__":
    main()
