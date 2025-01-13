import os
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain_community.chat_models import ChatOpenAI
from fpdf import FPDF

# Set OpenAI API key
os.environ["OPENAI_API_KEY"] = "your-api-key"

def sanitize_text(text):
    """Replace unsupported Unicode characters with equivalents."""
    replacements = {
        "\u2019": "'",  # Smart quote to regular quote
        "\u201c": '"',  # Left double quote to regular quote
        "\u201d": '"',  # Right double quote to regular quote
    }
    for key, value in replacements.items():
        text = text.replace(key, value)
    return text

def read_java_code(file_path):
    """Reads the Java code from the specified file."""
    with open(file_path, "r") as file:
        return file.read()

def process_workflow(gildedrose_code):
    """Processes the workflow using LangChain and returns the results."""
    # Define prompts
    requirements_prompt = PromptTemplate(
        input_variables=["code"],
        template="You are an agent that gathers software requirements. Analyze the following code and describe improvements or new requirements based on maintainability, scalability, and code quality:\n\n{code}\n\nBe specific in your observations and recommendations."
    )

    code_generation_prompt = PromptTemplate(
        input_variables=["requirements"],
        template="You are an expert software developer. Based on the following requirements, generate the required Java code improvements or refactor the code. Ensure clean and modular design, following best practices:\n\n{requirements}"
    )

    proposal_writing_prompt = PromptTemplate(
        input_variables=["code"],
        template="You are a technical writer. Based on the following updated code, write a clear and concise proposal explaining the improvements made, why they were necessary, and how they enhance the system. Keep the audience in mind as technical reviewers:\n\n{code}"
    )

    # Initialize OpenAI model
    llm = ChatOpenAI(model="gpt-3.5-turbo")

    # Create LLM Chains
    requirements_chain = LLMChain(llm=llm, prompt=requirements_prompt)
    code_generation_chain = LLMChain(llm=llm, prompt=code_generation_prompt)
    proposal_writing_chain = LLMChain(llm=llm, prompt=proposal_writing_prompt)

    # Run workflow
    requirements = requirements_chain.run({"code": gildedrose_code})
    improved_code = code_generation_chain.run({"requirements": requirements})
    proposal = proposal_writing_chain.run({"code": improved_code})

    return requirements, improved_code, proposal

def generate_pdf(requirements, improved_code, proposal, output_path):
    """Generates a PDF report with the workflow results."""
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Helvetica", size=12)

    # Sanitize and write content
    pdf.multi_cell(0, 10, "Requirements:\n" + sanitize_text(requirements))
    pdf.add_page()
    pdf.multi_cell(0, 10, "Improved Code:\n" + sanitize_text(improved_code))
    pdf.add_page()
    pdf.multi_cell(0, 10, "Proposal:\n" + sanitize_text(proposal))

    # Save PDF
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    pdf.output(output_path)

def main():
    """Main function to run the workflow."""
    # File paths
    project_root = os.path.dirname(os.path.abspath(__file__))
    java_code_path = os.path.join(project_root, "../src/main/java/com/gildedrose/GildedRose.java")
    output_pdf_path = os.path.join(project_root, "output/analysis.pdf")

    # Read Java code
    gildedrose_code = read_java_code(java_code_path)

    # Process workflow
    requirements, improved_code, proposal = process_workflow(gildedrose_code)

    # Generate PDF
    generate_pdf(requirements, improved_code, proposal, output_pdf_path)
    print(f"Analysis saved to {output_pdf_path}")

if __name__ == "__main__":
    main()
