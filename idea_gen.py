import openpyxl
import os
import subprocess

EXCEL_FILE = 'data.xlsx'

def generate_idea_with_mistral():
    prompt = (
        "Generate a trending YouTube video idea based on current cultural trends, YouTube trending topics, and analytics. "
        "Then elaborate the idea into a 3 to 5-minute YouTube script with a proper intro, body, and outro. "
        "Respond strictly in this format:\n"
        "IDEA: <Your idea title>\nSCRIPT: <Full video script>"
    )
    command = ['ollama', 'run', 'mistral', prompt]
    result = subprocess.run(command, capture_output=True, text=True)
    return result.stdout.strip()

def log_idea_to_excel(idea):
    if not os.path.exists(EXCEL_FILE):
        wb = openpyxl.Workbook()
        ws = wb.active
        ws.append(['Idea', 'Status'])
    else:
        wb = openpyxl.load_workbook(EXCEL_FILE)
        ws = wb.active

    ws.append([idea, 'Used'])
    wb.save(EXCEL_FILE)
    print(f'Saved and marked idea as "Used": {idea}')

def get_latest_idea_and_script():
    response = generate_idea_with_mistral()
    if not response or "IDEA:" not in response or "SCRIPT:" not in response:
        print("Failed to parse idea and script from model output.")
        return None, None

    idea = response.split("IDEA:")[1].split("SCRIPT:")[0].strip()
    script = response.split("SCRIPT:")[1].strip()

    log_idea_to_excel(idea)
    return idea, script

if __name__ == '__main__':
    idea, script = get_latest_idea_and_script()
    print("Idea:", idea)
    print("Script:", script)
