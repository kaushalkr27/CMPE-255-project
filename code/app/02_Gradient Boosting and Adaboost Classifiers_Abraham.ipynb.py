# -*- coding: utf-8 -*-
"""255_Project.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1oJ2uAesOwiWirU9Ox7i5fXsfrgqt9dhC

## Gradient Boosting and Adaboost Classifiers
"""

from sklearn.ensemble import AdaBoostClassifier
 from sklearn.ensemble import GradientBoostingClassifier

ad=AdaBoostClassifier()
gd=GradientBoostingClassifier()

ad.fit(x_train,y_train)
  pred_ad=ad.predict(x_test)
  test_score_ad=accuracy_score(y_test,pred_ad)
  train_score_ad=(y_train,ad.predict(x_train))
  print("Accuracy Score for train data of Ada Boost is",accuracy_score(y_test,pred_ad))
  print("Accuracy Score for test data of Ada boost is",y_train,ad.predict(x_train))

print(classification_report(y_test, pred_ad))

gd.fit(x_train,y_train)
  pred_gd=gd.predict(x_test)
  test_score_ad=accuracy_score(y_test,pred_gd)
  train_score_ad=(y_train,gd.predict(x_train))
  print("Accuracy Score for train data of gradient Boost is",accuracy_score(y_test,pred_gd))
  print("Accuracy Score for test data of gradient boost is",y_train,gd.predict(x_train))

#Random forest AUC Curve
from sklearn.metrics import roc_auc_score

fpr, tpr, _ = metrics.roc_curve(y_test, Y_pred_ran_for)

# KNN AUC Curve
fpr1, tpr1, _ = metrics.roc_curve(y_test,  y_hat)

#Logistic Regression AUC Curve
fpr_lr, tpr_lr, _ = metrics.roc_curve(y_test, predictions)

#Gradient Boosting and Ada Boost Classifiers
fpr_ad, tpr_ad, _ = metrics.roc_curve(y_test, pred_ad)

fpr_gd, tpr_gd, _ = metrics.roc_curve(y_test, pred_gd)






# calculate scores
RF_auc = roc_auc_score(y_test, Y_pred_ran_for)

knn_auc = roc_auc_score(y_test, y_hat)

Lr_Auc= roc_auc_score(y_test, predictions)

AD_AUC=roc_auc_score(y_test, pred_ad)

GD_AUC=roc_auc_score(y_test, pred_gd)


# summarize scores
print('Random Forest Prediction: ROC AUC=%.3f' % (RF_auc))
print('KNN: ROC AUC=%.3f' % (knn_auc))
print('Logistic Regression AUC: ROC AUC=%.3f' % (Lr_Auc))
print('ADA boost AUC: ROC AUC=%.3f' % (AD_AUC))
#print('Gradient Boosting AUC: ROC AUC=%.3f' % (GD_AUC))



# plot the roc curve for the model

plt.plot(fpr, tpr, linestyle='--', label='Random Forest Prediction: ROC AUC=%.3f' % (RF_auc))
plt.plot(fpr1, tpr1, linestyle='--',marker='*',label='KNN : ROC AUC=%.3f' % (knn_auc))
plt.plot(fpr_lr, tpr_lr, linestyle='--', label='LR : ROC AUC=%.3f' % (Lr_Auc))
plt.plot(fpr_ad, tpr_ad, linestyle='--',marker='*',label='ADA Boost: ROC AUC=%.3f' % (AD_AUC))
#plt.plot(fpr_gd, tpr_gd, linestyle='--', label='Gradient Boosting: ROC AUC=%.3f' % (GD_AUC))


# axis labels
plt.xlabel('FALSE POSITIVE RATE')
plt.ylabel('TRUE POSITIVE RATE')
# show the legend
plt.legend()
# show the plot
plt.show()