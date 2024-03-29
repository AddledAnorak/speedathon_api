from fastapi import FastAPI, Response

app = FastAPI()

@app.route('/first', methods=['GET', 'POST'])
def get_headers():
    headers = {
        'Content-Type': 'application/json',
        'Authorization': 'Bearer token123',
    }
    return Response(content='Hello, Headers!', headers=headers, status_code=200)

@app.route('/second', methods=['GET', 'POST'])
def get_headers():
    headers = {
        'Content-Type': 'application/json',
        'Authorization': 'Bearer token123',
    }
    return Response(content={
        'param1': 'value1',
        'param2': 'value2'
    }, headers=headers, status_code=400)