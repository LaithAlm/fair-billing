# Fair Billing

## Description
A Python application to calculate fair billing based on session logs with unit tests, availble to run from docker and python directly. 

## Setup

### Prerequisites
- Docker installed on your machine (for Docker run)
- Python installed on your machine (for direct run)

### External dependencies
- No external dependencies is needed.
- The empty file requirements.txt is created just for the project to be aware of Python’s package management practices and to help point out that there are no extrnal dependcies used here.

## Running with Docker
### Steps

1. **Clone the repository:**
```sh
   git clone https://github.com/LaithAlm/fair-billing.git
   cd fair-billing
```

2. **Build Docker Image:**
```sh
docker build -t fair-billing
```

3. **Run Tests:**
```sh
docker run fair-billing
```

4. **Create a Log Directory and Sample Log File (if not already in the cloned repo):**

```sh
mkdir -p logs
touch logs/sample_log.txt
```
Add the following content to logs/sample_log.txt:
```sh
14:02:03 ALICE99 Start
14:02:05 CHARLIE End
14:02:34 ALICE99 End
14:02:58 ALICE99 Start
14:03:02 CHARLIE Start
14:03:33 ALICE99 Start
14:03:35 ALICE99 End
14:03:37 CHARLIE End
14:04:05 ALICE99 End
14:04:23 ALICE99 End
14:04:41 CHARLIE Start
```

5. **Run Application:**
```sh
docker run -v $(pwd)/logs:/app/logs fair-billing python src/fair_billing.py /app/logs/sample_log.txt
```
6. **Check Output:**
The output should be:
ALICE99 4 240
CHARLIE 3 37


## Running Directly with Python
### Steps


1. **Clone the repository:**

```sh
git clone https://github.com/yourusername/fair-billing.git
cd fair-billing
```

2. **Run Application:**
- If you have Python 2 installed:
```sh
python src/fair_billing.py logs/sample_log.txt
```
You may wish to have the log file containing session logs as a different name or different place so amend it if you wish and then change the file path in the command.

- If you have Python 3 installed:
```sh
python3 src/fair_billing.py logs/sample_log.txt
```


The output should be:

```sh
ALICE99 4 240
CHARLIE 3 37
```

## Notes
- Ensure Docker is installed on your machine to build and run the Docker image.
- Ensure Python 3 is installed on your machine to run the application directly.
- The application reads a log file and calculates the total session time for each user.
- Invalid or irrelevant data in the log file is silently ignored.





