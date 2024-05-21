# Fair Billing

## Description
A Python application to calculate fair billing based on session logs.

## Setup

### Prerequisites
- Docker installed on your machine (for Docker run)
- Python installed on your machine (for direct run)

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

5. **Run Application:**
```sh
docker run -v $(pwd)/logs:/app/logs fair-billing python src/fair_billing.py /app/logs/sample_log.txt
```

6. **Output**
```sh
..
----------------------------------------------------------------------
Ran 2 tests in 0.003s

OK
```

7. **Check Output in a txt file:**
```sh
docker run -v $(pwd)/logs:/app/logs fair-billing python src/fair_billing.py /app/logs/sample_log.txt > output.txt
```
To view the txt file, either click on the new file if you are using Visual Studio Code, or you can view the file using:
```sh
cat output.txt
```

A new file should be created with the name output.txt and The output should be printed on your terminal if you have used the code above:
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
You may wish to have the log file containing session logs as a different name or different place so amend it if you wish.

- If you have Python 3 installed:
```sh
python3 src/fair_billing.py logs/sample_log.txt
```
## Check Output:
The output should be:

ALICE99 4 240

CHARLIE 3 37

## Notes
- Ensure Docker is installed on your machine to build and run the Docker image.
- Ensure Python 3 or 2 is installed on your machine to run the application directly.
- The application reads a log file and calculates the total session time for each user.
- Invalid or irrelevant data in the log file is silently ignored.

## Troubleshooting
### Common Issues
- Docker Build Issues: Ensure Docker is installed and running on your machine.
- Python Version Issues: Ensure Python 3 or 2 is installed and added to your PATH.













