from flask import Flask, render_template, request

app = Flask(__name__)

# 🔁 Dummy data generator simulating GPT results
def generate_response(prompt_type, idea):
    if prompt_type == "refine":
        return f"The startup idea '{idea}' can be refined by focusing on a niche market, validating demand with an MVP, and using modern tech for scaling."
    
    elif prompt_type == "pitch":
        return (
            "Slide 1: Problem\n"
            "Slide 2: Solution\n"
            "Slide 3: Market Opportunity\n"
            "Slide 4: Product Overview\n"
            "Slide 5: Business Model\n"
            "Slide 6: Traction & Roadmap\n"
            "Slide 7: The Ask (Funding, Team, etc.)"
        )
    
    elif prompt_type == "revenue":
        return "Revenue sources include subscriptions, freemium upgrades, data partnerships, and B2B licensing."
    
    elif prompt_type == "valuation":
        return "Based on projections and comparable startups, valuation could range from $500K to $2M at the early stage."
    
    elif prompt_type == "details":
        return (
            f"📌 Idea Overview:\n'{idea}' solves a real-world problem using innovation. It has potential if focused on the right audience.\n\n"
            f"🎯 Target Audience:\nDefine clearly — individuals, small businesses, or enterprises?\n\n"
            f"🧠 Technology Stack:\nIs it a mobile/web app? Does it involve AI, blockchain, or IoT?\n\n"
            f"💵 Monetization Strategy:\nSubscriptions, ads, affiliate commissions, or direct sales?\n\n"
            f"📊 Market Fit:\nResearch competitor gaps, user pain points, and potential for differentiation.\n\n"
            f"🚀 Execution Plan:\nPrototype → Validate → Build → Launch. Set key milestones and timelines."
        )
    
    return "Unknown section."

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate', methods=['POST'])
def generate():
    idea = request.form['idea']

    refined = generate_response("refine", idea)
    pitch = generate_response("pitch", idea)
    revenue = generate_response("revenue", idea)
    valuation = generate_response("valuation", idea)
    details = generate_response("details", idea)

    return render_template("results.html", idea=idea, refined=refined, pitch=pitch,
                           revenue=revenue, valuation=valuation, details=details)

if __name__ == '__main__':
    app.run(debug=True)
