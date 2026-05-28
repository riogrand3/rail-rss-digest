"""RSS feed configuration for Brendan's weekly rail intelligence report."""

RSS_FEEDS = {
    # General rail industry
    "Railway Insider": "http://www.railwayinsider.eu/wp/feed",
    "International Railway Journal": "https://www.railjournal.com/feed/",
    "Progressive Railroading": "http://www.progressiverailroading.com/rss/news.asp",
    "Railway News": "https://railway-news.com/feed/",

    # Add more later after the first successful test.
    # "Mass Transit Magazine": "https://www.masstransitmag.com/rss",
}

DIGEST_GENERATION_PROMPT = """
You are generating a twice-weekly rail-sector intelligence brief for Brendan Warner.

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
- MTA Long Island Rail Road
- MTA Metro-North Railroad
- NJ Transit
- WMATA / Washington Metro
- MBTA
- SEPTA
- Chicago Transit Authority / CTA
- Chicago Metra
- BART / Bay Area Rapid Transit
- LA Metro
- Caltrain
- Sound Transit
- MARTA
- DART / Dallas Area Rapid Transit
- RTD Denver
- Federal Railroad Administration / FRA
- Federal Transit Administration / FTA
- USDOT Build America Bureau
- Northeast Corridor Commission
- California State Transportation Agency / CalSTA and Caltrans Division of Rail and Mass Transportation
- Wabtec
- Knorr-Bremse
- ABB
- Schneider Electric
- TÜV SÜD
- TÜV Rheinland
- Bureau Veritas
- Applus+
- SGS

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
- investment into passenger rail in the USA

SOURCE MATERIAL:
ARTICLES FROM {date_range} ({article_count} articles):

{article_list}

TASK:
Create a concise rail intelligence brief. Do not write a generic news summary. Select and interpret the most relevant developments for Brendan.

ANTI-REPETITION RULES:
- Mention each article's basic facts only once.
- Do not repeat the same article in every section.
- Later sections must add new interpretation, not restate summaries.
- If an article has no clear relevance to SGS, Erion, rolling stock, maintenance, testing, or certification, keep it brief or omit it from detailed analysis.
- Group similar articles together instead of analyzing them separately.
- Avoid repeating company names, standards, or opportunities unless there is a new reason to mention them.
- Be concise. Prefer 1 strong paragraph over 5 weak bullets.

DUPLICATE HANDLING:
Some feeds may report the same story. Merge duplicate or near-duplicate articles into one development. If two articles cover the same event, cite both links together but analyze the story only once. Do not create separate priority briefings for duplicate versions of the same story.

SOURCE PRIORITY:
When multiple sources cover the same story, prefer the article with the most technical, operational, supplier-specific, maintenance-related, or certification-relevant detail. Do not give extra importance to a story only because it appears in multiple feeds.

RELEVANCE FILTER:
Only analyze articles in detail if they are relevant to at least one of:
- rolling stock
- material rodante
- maintenance
- depot/workshop operations
- traction systems
- motors
- converters, inverters, auxiliary power, batteries, chargers, UPS
- onboard electronics
- signalling, train control, ERTMS, ETCS, CBTC
- safety systems
- testing, inspection, certification, standards, homologation
- Spain, Europe, US passenger rail, or target companies

All other articles should appear only in the source list.

PRIORITY TOPICS:
Prioritize:
- rolling stock and fleet modernization
- material rodante
- depot/workshop technology
- maintenance, diagnostics, overhaul, inspections
- traction, converters, inverters, motors, auxiliary power, batteries, chargers, UPS
- onboard electronics
- signalling, ERTMS, ETCS, CBTC, train-control interfaces
- EMC, EN 50121, EN 50155, EN 61373, EN 45545
- environmental, shock/vibration, and fire testing
- testing, inspection, certification, homologation, conformity assessment
- Spanish, European, and US passenger rail
- suppliers, OEMs, operators, and fleet modernization programs

OUTPUT FORMAT:
Return clean semantic HTML only. Do not include html, head, or body tags.

Use this structure:

<h2>Executive summary</h2>
One short paragraph with the main pattern across the articles.

<h2>Priority briefings</h2>
Select only the 5 to 8 most important developments. For each:
<h3>Article title</h3>
<ul>
  <li><strong>What happened:</strong> factual summary in 1 sentence</li>
  <li><strong>Why it matters:</strong> practical rail-sector meaning</li>
  <li><strong>Relevance:</strong> High / Medium / Low</li>
  <li><strong>Main lens:</strong> rolling stock / maintenance / signalling / TIC / supplier / policy / safety / other</li>
</ul>

<h2>Cross-cutting patterns</h2>
Do not repeat article summaries. Identify 2 to 4 patterns across the week, such as fleet renewal, signalling modernization, safety, certification demand, maintenance technology, supplier movement, or digitalization.

<h2>SGS Tecnos / TIC relevance</h2>
Only discuss articles with a plausible testing, inspection, certification, conformity assessment, EMC, environmental, mechanical, fire, or standards angle.
For each relevant theme, include:
<ul>
  <li><strong>Possible TIC angle:</strong></li>
  <li><strong>Standards possibly involved:</strong></li>
  <li><strong>Confidence:</strong> High / Medium / Low</li>
  <li><strong>Follow-up question:</strong></li>
</ul>
Be conservative. Do not invent SGS capabilities, clients, or opportunities.

<h2>Erion / technician learning</h2>
Do not repeat news summaries. Translate the week into practical learning prompts:
<ul>
  <li><strong>Ask:</strong> questions to ask experienced technicians</li>
  <li><strong>Observe:</strong> systems, components, procedures, or failure modes to watch</li>
  <li><strong>Vocabulary:</strong> Spanish / English technical terms to learn</li>
</ul>

<h2>Suggested actions before the next report</h2>
Give 5 concrete actions. Keep them realistic for someone working/studying in Madrid.

<h2>Source list</h2>
List every article considered, with clickable title, feed name, and date. If multiple articles covered the same story, group them under the same source-list item where practical.

STYLE:
- Direct, technical, and concise.
- No hype.
- No repeated explanations.
- Separate confirmed facts from possible implications.
- Use cautious language: "possible", "may indicate", "worth watching", "not confirmed by the article".
"""
