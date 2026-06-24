import sys
import re
import time
import random

class HakiLegalChatbot:
    """
    A chatbot providing basic guidance on Kenyan Labor Laws and Tenant Rights.
    Disclaimer: This is for informational purposes and not professional legal advice.
    """

    def __init__(self):
        self.knowledge_base = {
            "labor_leave": {
                "keywords": ["leave", "vacation", "off day", "maternity", "paternity"],
                "response": "Under the Kenyan Employment Act, employees are entitled to 21 working days of annual leave with full pay. Maternity leave is 3 months, and paternity leave is 2 weeks (14 days)."
            },
            "labor_termination": {
                "keywords": ["fired", "terminated", "dismissed", "notice", "redundancy"],
                "response": "For termination, notice periods depend on your contract. Generally, if paid monthly, a 1-month written notice or 1-month pay in lieu of notice is required. Termination must be fair and follow due process (Section 41)."
            },
            "labor_wage": {
                "keywords": ["salary", "wage", "minimum pay", "overtime"],
                "response": "Minimum wage in Kenya varies by sector and location (e.g., Nairobi vs. rural). As of late 2022/2023, the general minimum wage for unskilled employees was increased by 12%. Check the latest Regulation of Wages Order for your specific industry."
            },
            "tenant_eviction": {
                "keywords": ["evict", "kicked out", "throwing out", "lock"],
                "response": "A landlord cannot arbitrarily evict you or lock your house. They must issue a formal notice (usually 30 days) and obtain a court order or go through the Rent Restriction Tribunal if the rent is below a certain threshold."
            },
            "tenant_deposit": {
                "keywords": ["deposit", "refund", "security"],
                "response": "Rent deposits should be refunded upon moving out, provided there are no damages beyond fair wear and tear and all bills are paid. Landlords often require a 30-day notice before moving out to process refunds."
            },
            "tenant_rent_increase": {
                "keywords": ["rent increase", "more money", "hike"],
                "response": "A landlord must provide a formal 'Notice of Increase of Rent' (usually 90 days notice). You have the right to challenge unreasonable increases at the Rent Restriction Tribunal."
            }
        }
        self.exit_commands = ["exit", "quit", "bye", "asante", "stop"]

    def get_response(self, user_input):
        user_input = user_input.lower()
        
        # Check for exit
        if any(cmd in user_input for cmd in self.exit_commands):
            return "Goodbye! Stay informed about your rights (Haki)."

        # Basic matching logic
        for intent, data in self.knowledge_base.items():
            for keyword in data["keywords"]:
                if re.search(r'\b' + re.escape(keyword) + r'\b', user_input):
                    return data["response"]
        
        return "I'm sorry, I don't have specific details on that. Try asking about leave, termination, minimum wage, eviction, or rent deposits."

    def start(self):
        print("="*60)
        print("HAKI LEGAL CHATBOT - KENYA (2026 Edition)")
        print("Basic Guidance on Labor Laws & Tenant Rights")
        print("Type 'exit' to quit.")
        print("="*60)
        
        while True:
            try:
                user_query = input("\nYou: ").strip()
                if not user_query:
                    continue
                
                print("HakiBot is thinking...", end="\r")
                time.sleep(0.6)
                
                response = self.get_response(user_query)
                print(f"HakiBot: {response}")
                
                if any(cmd in user_query.lower() for cmd in self.exit_commands):
                    break
            except KeyboardInterrupt:
                print("\nSession terminated.")
                break

if __name__ == "__main__":
    bot = HakiLegalChatbot()
    bot.start()