# 🔄 JSON to ENV

A lightweight Python CLI tool that converts JSON configuration data into `.env` format.

## Features

- Convert JSON objects to environment variables
- Automatically uppercase keys
- Handle strings, numbers and booleans
- Validate JSON input
- No external dependencies

## Run

```bash
python main.py
```

## Example

Input:

```json
{"api_key":"demo123","port":8000,"debug":true}
```

Output:

```env
API_KEY=demo123
PORT=8000
DEBUG=true
```

## Built With

- Python
- JSON
