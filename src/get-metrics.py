from sklearn.metrics import (make_scorer, matthews_corrcoef, classification_report, roc_curve, auc, 
                             accuracy_score, precision_score, recall_score, f1_score, confusion_matrix, 
                             multilabel_confusion_matrix, ConfusionMatrixDisplay)
def get_regression_metrics(model, dataframe, X, y_true):
    """
    Get a dictionary w/ metrics: 'model' is sklearn model w/ predict method,
    'X' is dataframe(FEATURES), 'y' is dataframe(TARGET)
    """
    y_pred = model.predict(X)

    f1 = f1_score(y_true, y_pred, average= 'macro', zero_division=0)
    f1_weighted = f1_score(y_true, y_pred, average= 'weighted', zero_division=0)
    mcc = matthews_corrcoef(y_true, y_pred)
    acc = accuracy_score(y_true, y_pred)
    prec = precision_score(y_true, y_pred, average='macro', zero_division=0) # Add zero_division=0 to handle cases with no positive predictions
    rec = recall_score(y_true, y_pred, average='macro', zero_division=0)
    prec_weighted = precision_score(y_true, y_pred, average='weighted', zero_division=0) # Add zero_division=0 to handle cases with no positive predictions
    rec_weighted = recall_score(y_true, y_pred, average='weighted', zero_division=0)
        
    #confusion = confusion_matrix(y_true, model.predict(X), normalize='true')
    #report = classification_report(y_true, y_pred, zero_division=0)
    # ^ bring these back later

    metrics_dict = {
        'F1': f1, # weighted average of the F1 scores of each class
        'weighted F1': f1_weighted, # 
        'MCC': mcc, # multiclass mcc   
        'accuracy': acc, #
        'precision':  prec, # 
        'weighted precision': prec_weighted,
        'recall': rec,
        'weighted recall': rec_weighted
      #  'confusion matrix': confusion,
      #  'classification_report': report
      # bring these back ater ^
    }

    return metrics_dict