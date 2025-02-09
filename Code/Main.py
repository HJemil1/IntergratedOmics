import argparse
from copy import copy
import Reader
import Elasticnet
import sys
import Visualisations
import Metrics
import Logging

def main():
    # Parse commandline arguments
    parser = argparse.ArgumentParser()
    parser.add_argument("-f", help="File to be read", type=str, required=True)
    parser.add_argument("-head", help="Confirm if a header exists in the file", type=int, required=True)
    parser.add_argument("-ML_type", help="Output file", type=str, required=True)
    args = parser.parse_args()

    # Read the data provided via the commandline
    read = Reader.Reader(args.f, args.head)
    data = read.reader()

    if args.ML_type == "Elasticnet":
        try:
            algorithm = Elasticnet.Elasticnet(data, 'BMI')
            algorithm.extract_labels()
            X_train, X_test, y_train, y_test = algorithm.split_data()
            elastic_model = algorithm.train_model(X_train, y_train)
            predictions = algorithm.predict(elastic_model, X_test)
            model, cv = algorithm.define_model()
            scores = algorithm.evaluate_model(model, cv)
            metrics = Metrics.Metrics(y_test, predictions)
            r2 = metrics.r_squared()
            mse = metrics.mean_squared_error()
            mae = metrics.mean_absolute_error()
            rmse = metrics.root_mean_squared_error()
            print("Input file: %s" % args.f)

            # Data preparation for plotting(should become a class)
            scores1 = copy(scores)
            scores2 = {"Algorithm1": scores, "Algorithm2": scores1}
            #
            visuals = Visualisations.Visualisations(scores2, cv)
            visuals.boxplot()
        except:
            print("Error: Elasticnet failed")
            sys.exit(1)

    elif args.ML_type == "XG":
        try:
            pass
        except:
            print("Error: XG failed")
            sys.exit(1)

        # algorithm = xgboost_algorithm.XG(data, 'BMI')
        # algorithm.XG_boost(data, 'BMI')

    elif args.ML_type == "etcetera":
        print("etcetera")

    else:
        print("Please specify a valid ML type")  # raise exception?
        sys.exit()


if __name__ == "__main__":
    sys.exit(main())
