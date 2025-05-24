# GPT Model Switcher

Python script that analyzes input token count to dynamically choose between GPT-3.5 and GPT-4. Designed to classify customer profiles from a purchase list using OpenAI's chat API.

## 🚀 How to Run

1. Clone the repo  
2. Install dependencies:  
   ```bash
   pip install -r requirements.txt
   ```

3. Create a `.env` file with your API key:  
   ```
   OPENAI_API_KEY=your_openai_api_key_here
   ```

4. Add your CSV input file in the `data` folder, named:
   ```
   purchase_list_100_customers.csv
   ```

5. Run the script:  
   ```bash
   python gpt_model_switcher.py
   ```

## 🧠 What it Does

- Loads a customer purchase list from a CSV  
- Estimates total input tokens using `tiktoken`  
- If input size exceeds GPT-3.5 token limit, switches to GPT-4  
- Sends prompt to the selected model  
- Outputs concise customer profiles

## ⚠️ Notes

- `output_tokens_expected` is set to 2048 by default — adjust if needed  
- The script assumes a fixed input/output token limit; not adaptive to price/performance trade-offs  
- Requires internet access and a valid OpenAI API key

## 📄 License

MIT
