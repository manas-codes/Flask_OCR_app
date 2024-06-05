from flask import Flask, request, jsonify
from PIL import Image
import base64
import io
from tesseract import image_to_text, image_to_bboxes

app = Flask(__name__)


@app.route('/api/get-text', methods=['POST'])
def get_text():
    try:
        data = request.json
        base64_image = data.get('base64_image')

        if not base64_image:
            return jsonify({
                'success': False,
                'error': {'message': 'Missing base64_image.'}
            }), 400

        try:
            image_data = base64.b64decode(base64_image)
            image = Image.open(io.BytesIO(image_data))
        except Exception as e:
            return jsonify({
                'success': False,
                'error': {'message': 'Invalid base64_image.'}
            }), 400

        text = image_to_text(image)
        return jsonify({
            'success': True,
            'result': {'text': text}
        })

    except Exception as e:
        return jsonify({
            'success': False,
            'error': {'message': 'An error occurred while processing the image.'}
        }), 500

@app.route('/api/get-bboxes', methods=['POST'])
def get_bboxes():
    try:
        data = request.json
        base64_image = data.get('base64_image')
        bbox_type = data.get('bbox_type', 'word')

        if not base64_image:
            return jsonify({
                'success': False,
                'error': {'message': 'Missing base64_image.'}
            }), 400

        if bbox_type not in ['word', 'line', 'paragraph', 'block', 'page']:
            return jsonify({
                'success': False,
                'error': {'message': 'Invalid bbox_type.'}
            }), 400

        try:
            image_data = base64.b64decode(base64_image)
            image = Image.open(io.BytesIO(image_data))
        except Exception as e:
            return jsonify({
                'success': False,
                'error': {'message': 'Invalid base64_image.'}
            }), 400

        bboxes = image_to_bboxes(image, bbox_type)
        return jsonify({
            'success': True,
            'result': {'bboxes': bboxes}
        })

    except Exception as e:
        return jsonify({
            'success': False,
            'error': {'message': 'An error occurred while processing the image.'}
        }), 500

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=8000)

