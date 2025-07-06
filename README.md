## Setup & Run Guide

### Requirements

- Python 3.12+
- [uv](https://github.com/astral-sh/uv) (a drop-in replacement for pip + venv)

---

### 1. Clone & Navigate

```bash
git clone <your-repo-url>
cd fitnessapp
````

---

### 2. Install `uv` (if not already installed)

```bash
curl -Ls https://astral.sh/uv/install.sh | sh
```

Or with pipx:

```bash
pipx install uv
```

---

### 3. Create Virtual Environment

```bash
uv venv
```

optional

```bash
source .venv/bin/activate
```

---

### 4. Install Dependencies

```bash
uv pip install -r pyproject.toml
```

---


_Before Running Make sure you have `.env` file_

```.env
OPENAI_API_KEY=sk-proj-as......
```

### 5. Run the Application

```bash
uv run main.py
```

This will start the server on:

```
http://0.0.0.0:9000
```

* Open docs: `http://127.0.0.1:9000/docs`
* Test endpoint: `POST /predict`

---

## Docker Support

### Build Docker Image

```bash
docker build -t fitnessapp .
```

### Run Docker Container

```bash
docker run --env-file .env -p 9000:9000 fitnessapp
```

### use dockercompose (Optionaly)

```bash
docker-compose up --build

```


```bash
docker-compose down

```

---

## Project Structure

```
.
├── api.py
├── dockerfile
├── fitness_data_embedding.pickle
├── __init__.py
├── llm.py
├── main.py
├── pyproject.toml
├── README.md
├── req.json
├── utils.py
├── uv.lock
├── .env
```

---

## Notes

* Ensure you have an OpenAI API key configured if the app makes external API calls.
* The app starts with `uv run`, which behaves like `uvicorn main:app --reload` behind the scenes if your `main.py` defines `app`.


## Running streamlit webapp

```bash
streamlit run app.py
```

### Example Fitness goal:

```
User Fitness Profile
Age: 55–64
Gender: Female
Height: 5'0" – 5'4" (152–163 cm)
Current Weight: 150–174 lbs (68–79 kg)
Desired Weight: 100–124 lbs (45–56 kg)
BMI: 25–29.9 (Overweight)
Occupation Activity Level: Mostly sedentary (desk work/administrative)
Chronic Health Conditions: None
Dietary Preference: Vegetarian
Sleep Duration: 4–5 hours per night
Current Fitness Level: Intermediate
Current Exercise Frequency: Daily
Preferred Update Frequency: Daily
```