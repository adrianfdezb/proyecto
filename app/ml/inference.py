from joblib import load

clf = load('filename.joblib')

def make_inference(X):
    # formatear dattos
    # ...

    # hacer inferencia
    y_pred = clf.predict(X)

    # formatear prediccion
    prediccion = {
        valor: y_pred
    }

    return prediccion

