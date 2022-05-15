{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "ff79a2aa",
   "metadata": {},
   "outputs": [],
   "source": [
    "import numpy as np\n",
    "import matplotlib.pyplot as plt\n",
    "import pandas as pd\n",
    "import os\n",
    "from sklearn.model_selection import train_test_split\n",
    "from sklearn.preprocessing import StandardScaler\n",
    "from sklearn.linear_model import LogisticRegression\n",
    "from sklearn.metrics import confusion_matrix\n",
    "from sklearn.metrics import accuracy_score\n",
    "\n",
    "\n",
    " #############################################################\n",
    " # I was not sure whether I should also return a graphical representation\n",
    " # of the results. We should discuss whether we only are returning the \n",
    " # accuracy values for the boostin algorithms later or also some graphical \n",
    " # displays of the smaller ML. Perhaps it would be an overkill?\n",
    " #############################################################\n",
    "\n",
    "\n",
    "class Logistic regression:\n",
    "    def __init__(self, file, labelname):\n",
    "        self.file = file\n",
    "        self.labelname = labelname\n",
    "        self.labels = None\n",
    "        \n",
    "    def extract_labels(self):\n",
    "        self.file = self.file.dropna(axis=0)\n",
    "        self.labels = self.file[self.labelname]\n",
    "        self.file = self.file.drop([self.labelname, \"Pseudo\", \"Antibody_batch\"], axis=1)\n",
    "    \n",
    "    def split_data(self):\n",
    "        X = self.file.iloc[:, [0,2]].values  # Age and BMI columns\n",
    "        y = self.file.iloc[:, 1].values  # Gender\n",
    "        \n",
    "    def train_test_split(self):\n",
    "        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.25, random_state = 0)\n",
    "        \n",
    "    def scaling(self):\n",
    "        sc_X = StandardScaler()\n",
    "        X_train = sc_X.fit_transform(X_train)\n",
    "        X_test = sc_X.transform(X_test)\n",
    "        \n",
    "    def define_model(self):\n",
    "        classifier = LogisticRegression(random_state=0)\n",
    "        classifier.fit(X_train, y_train)\n",
    "    \n",
    "    def prediction(self):\n",
    "        y_pred = classifier.predict(X_test)   # obtain predictions\n",
    "        score =accuracy_score(y_test,y_pred)   # caculate accuracy\n",
    "        score = \"{:.2f}\".format(score)\n",
    "        cm = confusion_matrix(y_test, y_pred)  # get confusion matrix\n",
    "        print(\"Accuracy score logisitc regression:\",score, \"%\")\n",
    "        print(\"Confusion matrix:\", cm) # should I also include the confusion matrix?\n",
    "        \n",
    "    def graph_train(self):\n",
    "        X_set, y_set = X_train, y_train\n",
    "        X1, X2 = np.meshgrid(np.arange(start = X_set[:, 0].min() - 1, stop = X_set[:, 0].max() + 1,   step = 0.01),\n",
    "                     np.arange(start = X_set[:, 1].min() - 1, stop = X_set[:, 1].max() + 1, step = 0.01))\n",
    "        plt.contourf(X1, X2, classifier.predict(np.array([X1.ravel(), X2.ravel()]).T).reshape(X1.shape),\n",
    "             alpha = 0.75, cmap = ListedColormap(('red', 'green')))\n",
    "        plt.xlim(X1.min(), X1.max())\n",
    "        plt.ylim(X2.min(), X2.max())\n",
    "        for i, j in enumerate(np.unique(y_set)):\n",
    "        plt.scatter(X_set[y_set == j, 0], X_set[y_set == j, 1],\n",
    "                c = ListedColormap(('red', 'green'))(i), label = j)\n",
    "        plt.title('Logistic Regression (Train set)')\n",
    "        plt.xlabel('Age')\n",
    "        plt.ylabel('BMI')\n",
    "        plt.legend()\n",
    "        return plt.show()\n",
    "        \n",
    "    \n",
    "    def graph_test(self):\n",
    "        X_set, y_set = X_test, y_test\n",
    "        X1, X2 = np.meshgrid(np.arange(start = X_set[:, 0].min() - 1, stop = X_set[:, 0].max() + 1, step = 0.01),\n",
    "                     np.arange(start = X_set[:, 1].min() - 1, stop = X_set[:, 1].max() + 1, step = 0.01))\n",
    "        plt.contourf(X1, X2, classifier.predict(np.array([X1.ravel(), X2.ravel()]).T).reshape(X1.shape),\n",
    "             alpha = 0.75, cmap = ListedColormap(('red', 'green')))\n",
    "        plt.xlim(X1.min(), X1.max())\n",
    "        plt.ylim(X2.min(), X2.max())\n",
    "        for i, j in enumerate(np.unique(y_set)):\n",
    "            plt.scatter(X_set[y_set == j, 0], X_set[y_set == j, 1],\n",
    "                c = ListedColormap(('red', 'green'))(i), label = j)\n",
    "        plt.title('Logistic Regression (Test set)')\n",
    "        plt.xlabel('Age')\n",
    "        plt.ylabel('BMI')\n",
    "        plt.legend()\n",
    "        return plt.show()\n",
    "        \n",
    "        \n",
    "    \n",
    "    \n",
    "    "
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.9.7"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
