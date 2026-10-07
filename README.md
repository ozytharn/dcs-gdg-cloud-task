# Cloud Recruitment Task Artifacts

This folder contains the local project artifacts prepared for the DCS X GDG Cloud recruitment task.

## Included
- `portfolio/` — static website assets for the S3 bucket deployment task
- `lambda/greeting_function.py` — Lambda handler for the serverless greeting task
- `docs/` — submission documentation assets

## Local preview
Open `portfolio/index.html` in a browser, or run a small local web server:

```bash
cd portfolio
python -m http.server 8000
```

Then visit http://localhost:8000

## AWS deployment notes
To deploy the static site to S3, create a public bucket, enable static website hosting, and upload `index.html`, `style.css`, and the `assets` folder.

For the Lambda function, create a Python 3.x function, paste the handler code, and test it with a payload such as:

```json
{"name": "Alex"}
```

Expected output:

```json
{"message": "Hello Alex, welcome to Cloud Computing!"}
```

## Submission summary
This project was assembled locally and is ready to be deployed once AWS credentials and access are available.
