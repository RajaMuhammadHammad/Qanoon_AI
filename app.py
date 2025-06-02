from flask import Flask, render_template, request, jsonify
from search import LegalSearch
from gemini import generate_answer
from evaluation import evaluate_answer

app = Flask(__name__)
search_system = LegalSearch()

@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST" and request.headers.get("X-Requested-With") == "XMLHttpRequest":
        query = request.form.get("query", "").strip()
        if query:
            context_items = search_system.search(query)
            context = "\n".join([
                f"{doc['pdf_name']} (Page {doc['page_number']}): {doc['text']}" for doc in context_items
            ])

            # 🔹 Format the prompt here
            prompt = f"""
You are a Pakistani legal expert AI.

Given the following legal context and a user question, generate a structured response in HTML format.

---

### 📚 Context:
{context}

---

### ❓ Query:
{query}

---

### ✅ Format Instructions:
Respond in HTML like this:

<h3>1. Legal Basis</h3>
<p>Explain the law(s) involved — such as ordinance names, sections, and powers.</p>

<br><br>

<h3>2. Simple Explanation</h3>
<p>Break it down for a non-technical person.</p>

<br><br>

<h3>3. Practical Implications</h3>
<p>Who it affects (students, citizens, etc.) and how.</p>

<br><br>

<h3>4. Source References</h3>
<p>Quote exact section numbers, clauses, and page references.</p>

IMPORTANT: Do NOT return Markdown. Return HTML tags only, no styling required.
"""

            # 🔹 Send full prompt to Gemini
            answer = generate_answer(prompt)
            scores = evaluate_answer(answer, context_items)
            sources = [{"pdf_name": doc["pdf_name"], "page_number": doc["page_number"]} for doc in context_items]

            return jsonify({
                "answer": answer,   # This is now pre-formatted HTML
                "scores": scores,
                "sources": sources
            })

        return jsonify({"answer": "No query provided.", "scores": {}, "sources": []})

    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
