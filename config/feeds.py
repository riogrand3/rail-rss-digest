"""RSS feed configuration for Brendan's weekly rail intelligence report."""

RSS_FEEDS = {
    # General rail industry
    "Railway Gazette": "https://www.railwaygazette.com/rss",
    "International Railway Journal": "https://www.railjournal.com/feed/",
    "Global Railway Review": "https://www.globalrailwayreview.com/feed/",
    "RailTech": "https://www.railtech.com/feed/",

    # Add more later after the first successful test.
    # "Railway-News": "https://www.railway-news.com/feed/",
    # "Mass Transit Magazine": "https://www.masstransitmag.com/rss",
}

DIGEST_GENERATION_PROMPT = """
You are generating a weekly rail-sector intelligence report for Brendan Warner.

CONTEXT ABOUT BRENDAN:
Brendan is a mechanical engineer from the United States working in Madrid, Spain. He is developing a career in passenger rail, rolling stock maintenance, rail systems integration, testing, inspection, certification, and technical documentation.

He works at SGS Tecnos in Madrid, where he is helping develop a rail testing, inspection, and certification business line. He is especially interested in identifying realistic opportunities related to rolling stock electronic equipment, EMC, environmental testing, shock and vibration, fire safety, power electronics, suppliers, certification, conformity assessment, and standards-driven testing.

He is also working as a technician at Erion in Madrid. He wants practical guidance for making the most of time around experienced rail maintenance professionals: what to ask, what to observe, what systems to learn, what Spanish/English technical vocabulary to develop, and how to connect hands-on maintenance experience with future engineering, testing, certification, and systems-integration roles.

LONG-TERM CAREER DIRECTION:
Brendan is interested in roles such as:
- rolling stock systems integration engineer
- rail systems engineer
- rolling stock maintenance engineer
- equipment engineer
- testing / validation / verification engineer
- certification / conformity assessment engineer
- technical documentation or requirements engineer
- fleet modernization or depot/workshop technology specialist

Companies and organizations of interest include:
- SGS Tecnos
- Erion
- Renfe
- ADIF
- Metro de Madrid
- CAF
- Talgo
- Alstom
- Siemens Mobility
- Stadler
- Amtrak
- MTA / New York City Transit
- other passenger rail operators, OEMs, suppliers, and testing/certification bodies

PRIORITY TOPICS:
Prioritize articles related to:
- rolling stock
- material rodante
- fleet modernization
- depot and workshop technology
- maintenance, overhaul, inspection, diagnostics
- predictive maintenance and condition monitoring
- traction systems
- motors
- converters, inverters, auxiliary power, batteries, chargers, UPS
- onboard electronics
- signalling, ERTMS, ETCS, CBTC, train control
- EMC and EN 50121
- EN 50155
- EN 61373
- EN 45545
- environmental testing
- shock and vibration
- testing, inspection, certification, homologation, conformity assessment
- rail suppliers and component manufacturers
- Spanish and European rail projects
- Renfe, ADIF, Metro de Madrid, CAF, Talgo, Alstom, Siemens, Stadler

SOURCE MATERIAL:
ARTICLES FROM {date_range} ({article_count} articles):
{article_list}

TASK:
Analyze the articles and create a weekly intelligence report.

IMPORTANT RULES:
- Do not invent facts.
- Use only the article information provided.
- Clearly separate confirmed facts from possible implications.
- Do not claim that something is an SGS opportunity unless the article supports it.
- Do not invent details about SGS Tecnos, Erion, their clients, equipment, contracts, or internal procedures.
- If relevance is speculative, say “possible relevance” or “potential implication.”
- Favor concrete, practical analysis over generic commentary.
- Each article should appear only once in the main report unless it is necessary to cross-reference it.
- Include links to article titles where possible.
- Return only clean HTML content for the digest body. Do not include html/head/body tags.

REPORT STRUCTURE:

## 1. Executive summary
Write one concise paragraph explaining the most important rail-sector themes this week.

## 2. Most important developments
Select the most important articles. For each:
- Article title as a clickable link
- What happened
- Why it matters
- Relevance level: High / Medium / Low
- Primary theme: rolling stock, maintenance, signalling, certification, infrastructure, market, policy, etc.

## 3. Spain / Europe relevance
Identify developments relevant to Spain, the EU, European rail suppliers, operators, regulation, procurement, fleet modernization, or standards.

## 4. Rolling stock, maintenance, and systems relevance
Explain what the articles suggest about rolling stock technology, maintenance practice, fleet modernization, diagnostics, workshops, depots, systems integration, traction, auxiliary systems, braking, doors, HVAC, onboard electronics, or signalling interfaces.

## 5. Testing, inspection, certification, and SGS Tecnos relevance
For relevant articles, explain possible implications for a testing/inspection/certification company developing rail-sector capabilities.

Use this format where useful:
- Possible testing/certification angle:
- Standards likely involved:
- Type of supplier/operator affected:
- Possible commercial relevance:
- Confidence level:
- Follow-up question for SGS:

Be conservative. Avoid overclaiming.

## 6. Erion / technician learning opportunities this week
Translate the week’s developments into practical learning actions for someone working around rail maintenance professionals at Erion.

Include:
- What Brendan should ask experienced technicians
- What systems/components he should observe
- What maintenance or diagnostic procedures he should try to understand
- Spanish/English vocabulary to learn
- How the hands-on learning connects to future engineering, testing, certification, or systems-integration work

Make this section practical and specific.

## 7. Professional development implications
Explain what Brendan should learn, study, or pay attention to based on this week’s news.

Include:
- technical topics to study
- standards to review
- companies to follow
- job-role relevance
- skills that connect workshop experience to engineering work

## 8. Suggested actions for next week
Give 5-10 concrete actions. Separate them into:
- At SGS
- At Erion
- Personal study
- Networking / companies to follow

## 9. Source list
List the articles used, grouped by source/feed.

FORMATTING:
Use clean, semantic HTML:
- Use <h2> for main sections
- Use <h3> for subsections
- Use <p> for paragraphs
- Use <ul> and <li> for lists
- Use <a href=""> for article links
- Do not use markdown
"""
