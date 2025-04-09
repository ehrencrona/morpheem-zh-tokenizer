from flask import Flask, request, jsonify
import jieba

app = Flask(__name__)

@app.route('/segment', methods=['POST'])
def segment_text():
    data = request.get_json()
    
    if not data or 'text' not in data:
        return jsonify({'error': 'Missing text parameter'}), 400
    
    input_text = data['text']
    
    # Segment the Chinese text
    seg_list = jieba.cut(input_text, cut_all=False)

    # Convert to list for JSON serialization
    result = list(seg_list)

    print(f"{input_text} -> {', '.join(result)}")
        
    return jsonify({'segments': result})

@app.route('/', methods=['GET'])
def health_check():
    return jsonify({'status': 'healthy'}), 200

if __name__ == '__main__':
    import os
    port = int(os.environ.get('PORT', 8000))
    app.run(host='0.0.0.0', port=port)
    