Hilal Khan Nasir - BSCS23001
# Instructions
## Environment Variable Setup
-->Create a .env file in frontend/ and one .env file in backend/src/
-->frontend/.env should have a VITE_CLERK_PUBLISHABLE_KEY field with the CLERK publishable key obtained by making a webapp instance on clerk
-->backend/.env should have CLERK_SECRET_KEY,CLERK_WEBHOOK_SECRET,JWT_KEY from Clerk and GROQ_API_KEY from openai groq for LLM query.
## Running the setup
-->Open 3 terminals
-->cd to backend folder in 1st terminal.
-->run the following command: uv run server.py
-->Go to 2nd Terminal. run:  ngrok http 8000
-->cd to frontend in 3rd terminal.
-->run: npm run dev
-->Click on the link generated. The web app frontend should load up.
