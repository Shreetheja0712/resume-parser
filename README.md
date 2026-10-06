# Resume Parser

A small Python script that uses Gemini's OpenAI-compatible API to extract structured information from a plain-text resume.

## What it extracts

The parser returns:

- Name
- Email address
- Phone number
- Skills
- Work experience, including company, role, and duration
- Education, including institution, degree, and year
- Projects, including name and description

The response is validated with Pydantic models before it is printed.

## Requirements

- Python 3.10 or newer
- A Gemini API key with access to the configured model

## Setup

1. Create and activate a virtual environment:

   ```powershell
   python -m venv .venv
   .\.venv\Scripts\Activate.ps1
   ```

2. Install the dependencies:

   ```powershell
   python -m pip install -r requirements.txt
   ```

3. Create a `.env` file in the project directory:

   ```dotenv
   GEMINI_API_KEY=your-gemini-api-key
   ```

   Keep the key private and do not commit the `.env` file.

## Usage

Place the resume text to parse in `resume.txt`, then run:

```powershell
python resume_parser.py
```

The parsed fields are printed to the console. The script currently uses the Gemini OpenAI-compatible endpoint and the `gemini-3.5-flash-lite` model configured in `resume_parser.py`.

## Input format

`resume.txt` should contain plain text. The parser does not currently accept PDF or DOCX files directly.

## Project files

| File | Purpose |
| --- | --- |
| `resume_parser.py` | Defines the response schema, calls Gemini, and prints the parsed result |
| `resume.txt` | Resume text supplied to the parser |
| `.env` | Local API key configuration |
| `requirements.txt` | Python runtime dependencies |

## Troubleshooting

- **Missing API key:** Confirm that `.env` contains `GEMINI_API_KEY` and that it is loaded from the project directory.
- **Missing resume:** Confirm that `resume.txt` exists beside `resume_parser.py`.
- **API or model errors:** Verify the API key, model availability, and network access to the Gemini endpoint.