from flask import Flask, request, jsonify
import boto3
import os

app = Flask(__name__)

# AWS S3 configuration
s3 = boto3.client('s3')

S3_BUCKET = os.getenv('S3_BUCKET')  # bucket where files are stored

@app.route('/api/v1/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return jsonify({"error": "No file provided"}), 400

    file = request.files['file']

    if file.filename == '':
        return jsonify({"error": "No selected file"}), 400

    if file and file.filename.endswith('.csv'):
        try:
            # Uploads the file to S3
            s3.upload_fileobj(file, S3_BUCKET, file.filename)
            
    #        # Returns succeed message
            return jsonify({"message": f"File {file.filename} successfully uploaded to S3."}), 200
        except Exception as e:
            return jsonify({"error": f"Failed to upload file: {str(e)}"}), 500

    return jsonify({"error": "Invalid file format. Please upload a CSV file."}), 400

    return jsonify({"message": "Ran ok"},200)
if __name__ == '__main__':
    app.run(debug=True)