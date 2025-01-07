from flask import Flask, render_template, request, jsonify
import mlflow.pyfunc
import mlflow
import pandas as pd

app = Flask(__name__)
# Set tracking URI dari environment variable
tracking_uri = "http://mlflow:8080"  # Arahkan ke service MLflow di docker-compose
mlflow.set_tracking_uri(tracking_uri)
model_uri = "runs:/cfb987e098e54119bdab9bb99bcab877/With tuning"
model = mlflow.pyfunc.load_model(model_uri)


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Ambil data dari request JSON
        data = request.json
        # Validasi keberadaan semua key yang diperlukan
        required_keys = ['Socioeconomic Score', 'Study Hours', 'Sleep Hours', 'Attendance (%)']
        if not all(key in data for key in required_keys):
            return jsonify({'error': 'Invalid input. Please provide all required fields.'}), 400

        # Ambil data dari JSON dan konversi ke tipe numerik
        try:
            study_hours = float(data['Study Hours'])
            sleep_hours = float(data['Sleep Hours'])
            socioeconomic_score = float(data['Socioeconomic Score'])
            attendance = float(data['Attendance (%)'])
        except ValueError:
            return jsonify({'error': 'All input values must be numeric.'}), 400

        # Siapkan input untuk model (menggunakan Pandas DataFrame)
        input_data = pd.DataFrame([{
            'Socioeconomic Score': socioeconomic_score,
            'Study Hours': study_hours,
            'Sleep Hours': sleep_hours,
            'Attendance (%)': attendance
        }])

        # Prediksi menggunakan model
        prediction = model.predict(input_data)

        # Return hasil prediksi
        return jsonify({'result': float(prediction[0])})

    except Exception as e:
        # Tangani error internal
        return jsonify({'error': str(e)}), 500

    except Exception as e:
        # Tangani error internal
        return jsonify({'error': str(e)}), 500


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
