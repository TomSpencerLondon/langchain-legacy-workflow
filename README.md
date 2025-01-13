# Gilded Rose starting position in Java

## Run the TextTest Fixture from Command-Line

```
./gradlew -q text
```

### Specify Number of Days

For e.g. 10 days:

```
./gradlew -q text --args 10
```

You should make sure the gradle commands shown above work when you execute them in a terminal before trying to use TextTest (see below).


## Run the TextTest approval test that comes with this project

There are instructions in the [TextTest Readme](../texttests/README.md) for setting up TextTest. What's unusual for the Java version is there are two executables listed in [config.gr](../texttests/config.gr) for Java. The first uses Gradle wrapped in a python script. Uncomment these lines to use it:

    executable:${TEXTTEST_HOME}/Java/texttest_rig.py
    interpreter:python

The other relies on your CLASSPATH being set correctly in [environment.gr](../texttests/environment.gr). Uncomment these lines to use it instead:

    executable:com.gildedrose.TexttestFixture
    interpreter:java


Here’s a comprehensive **README** for your project:

---

# **GildedRose Workflow with LangChain**

This project processes the Java `GildedRose` code using OpenAI's language models via the LangChain framework. The workflow generates insights, proposes improvements, and documents the results in a PDF file.

## **Features**
- **Requirements Analysis**: Extracts areas of improvement for the Java `GildedRose` code.
- **Code Generation**: Proposes and generates refactored code based on identified requirements.
- **Proposal Writing**: Creates a detailed proposal explaining the changes and their benefits.
- **PDF Report Generation**: Outputs the results (requirements, improvements, and proposal) to a neatly formatted PDF.

---

## **Setup Instructions**

### **1. Prerequisites**
- Python 3.12 or above
- OpenAI API key ([Get your API key here](https://platform.openai.com/account/api-keys))
- The `GildedRose.java` file in the correct directory:
  ```
  src/main/java/com/gildedrose/GildedRose.java
  ```

---

### **2. Install Dependencies**
1. Clone the repository:
   ```bash
   git clone https://github.com/your-repo/gilded-rose-langchain.git
   cd gilded-rose-langchain
   ```

2. Create a virtual environment and activate it:
   ```bash
   python3.12 -m venv venv
   source venv/bin/activate
   ```

3. Install the required Python packages:
   ```bash
   pip install langchain langchain-community langchain-openai fpdf
   ```

---

### **3. Configure the API Key**
Add your OpenAI API key in the `main.py` script by replacing `your-api-key`:
```python
os.environ["OPENAI_API_KEY"] = "your-api-key"
```

Alternatively, set the API key as an environment variable:
```bash
export OPENAI_API_KEY="your-api-key"
```

---

### **4. Run the Script**
Execute the script to analyze the Java code and generate the PDF report:
```bash
python main.py
```

---

## **Directory Structure**
```
gilded-rose-langchain/
├── main.py                 # Main Python script
├── output/                 # Directory for generated PDFs
│   └── analysis.pdf        # Output PDF report
├── requirements.txt        # List of dependencies
└── src/
    └── main/
        └── java/
            └── com/
                └── gildedrose/
                    └── GildedRose.java  # Input Java code
```

---

## **Expected Output**
The script generates a PDF file containing:
1. **Requirements**: Areas of improvement for the Java code.
2. **Improved Code**: Refactored or improved Java code.
3. **Proposal**: A concise explanation of the changes and their benefits.

The output PDF is saved to:
```
output/analysis.pdf
```

---

## **Example PDF Output**
```
Requirements:
- Improve scalability by refactoring repetitive conditionals.
- Enhance readability by introducing helper methods.

Improved Code:
... (Generated Java code here) ...

Proposal:
The proposed changes simplify the logic by refactoring repeated conditionals into helper methods, improving maintainability and scalability.
```

---

## **Troubleshooting**

### **Common Errors**
1. **`ModuleNotFoundError` for `langchain_community`**:
    - Ensure `langchain-community` is installed:
      ```bash
      pip install langchain-community
      ```

2. **`UnicodeEncodeError` in PDF Generation**:
    - The script sanitizes unsupported characters by default. Ensure you are using `Helvetica` or another supported font.

3. **`OpenAI API Error`**:
    - Check your OpenAI usage limits and API key permissions in the [OpenAI Dashboard](https://platform.openai.com/account/usage).

---

## **Acknowledgments**
- [LangChain](https://github.com/langchain-ai/langchain): For simplifying the integration of LLMs.
- [FPDF](http://www.fpdf.org/): For generating PDF reports.
- [OpenAI](https://openai.com/): For the GPT-3.5-turbo model.

---
