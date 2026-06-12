"""RSS feed configuration for Brendan's weekly rail intelligence report."""

RSS_FEEDS = {
    # Core global / international rail news
    "Railway-News": "https://railway-news.com/feed/",
    "Global Mass Transit": "https://globalmasstransit.net/feed",
    "Railway Pro": "https://www.railwaypro.com/wp/feed/",
    "Railcolor News": "https://railcolornews.com/feed/",
    "Railways Africa": "https://www.railways.africa/feed/",

    # USA passenger rail / commuter rail / transit / infrastructure
    "Progressive Railroading News": "https://www.progressiverailroading.com/rss/prnews.asp",
    "Railway Age": "https://www.railwayage.com/feed/",
    "Railway Track & Structures": "https://www.rtands.com/feed/",
    "METRO Magazine": "https://www.metro-magazine.com/rss",
    "Rail Pace": "https://railpace.com/feed/",
    "Streetsblog USA": "https://usa.streetsblog.org/feed",

    # Spain / Spanish-language rail and transport
    "Trenvista English": "https://www.trenvista.net/en/feed/",
    "El Mercantil": "https://elmercantil.com/feed/",

    # Europe / UK rail, policy, regulation, and operations
    "Rail Business Daily": "https://news.railbusinessdaily.com/feed/",
    "Rail Engineer": "https://www.railengineer.co.uk/feed/",
    "ORR News": "https://www.orr.gov.uk/taxonomy/term/110/feed",
    "Rail Delivery Group News": "https://media.raildeliverygroup.com/feed/rss",
    "Europe's Rail": "https://rail-research.europa.eu/feed/",
    "ERA News": "https://www.era.europa.eu/events-news/news_en.xml",

    # Safety / standards / technology / supplier-adjacent
    "ETSC": "https://etsc.eu/feed",
    "Cervello Security": "https://cervello.security/feed/",
    "ITDP Blog": "https://itdp.org/feed",
    
}

DIGEST_GENERATION_PROMPT = """
You are generating a twice-weekly rail-sector intelligence report for Brendan Warner.

Brendan is a mechanical engineer in Madrid working between rail testing/certification work at SGS Tecnos and hands-on rail maintenance exposure at Erion. He is interested in passenger rail, rolling stock, maintenance, systems integration, testing, inspection, certification, technical documentation, fleet modernization, and future rail engineering roles.

SOURCE MATERIAL:
ARTICLES FROM {date_range} ({article_count} articles):

{article_list}

TASK:
Create a structured rail-sector intelligence report using all of the article information provided.

The report must have four main purposes:
1. Select and summarize the top 20 most relevant rail-sector events from the source material.
2. Analyze global rail-sector trends based on the full article set, not only the top 20.
3. Analyze USA passenger rail / transit trends based on the full article set, not only the top 20.
4. Identify possible implications for SGS Tecnos in Madrid and for Brendan's future skills/training only when the full article set supports that analysis.

IMPORTANT DISTINCTION:
- The "Top 20 relevant rail-sector events" section should contain only the 20 most relevant events.
- The later analysis sections should consider all articles that were provided, including lower-ranked articles that do not appear in the Top 20.
- Do not pretend the Top 20 list is the entire dataset.
- If a lower-ranked article supports an important trend, you may mention it in the trend analysis even if it was not selected for the Top 20.

IMPORTANT RULES:
- Use only the article information provided.
- Do not invent facts, contracts, internal company information, technical details, or private strategy.
- Clearly separate confirmed article facts from possible implications.
- Use cautious language: "may indicate", "possible implication", "worth watching", "not confirmed by the article".
- Do not overstate SGS relevance.
- If there are no relevant SGS Tecnos implications, say so directly.
- If the source material does not support a skills/training projection, omit that section or state that no clear training signal is present.
- Do not repeat the same article summary in multiple sections.
- Mention the basic facts of each article only once.
- Merge duplicate or near-duplicate articles into one event.
- If multiple sources cover the same event, cite/link them together under the same event.
- Do not give extra importance to an event only because it appears in multiple feeds.
- Prefer the source with the most technical, operational, supplier-specific, maintenance-related, or certification-relevant detail.

RELEVANCE PRIORITIES:
When selecting the top 20 events, prioritize articles related to:
- rolling stock
- fleet modernization
- material rodante
- passenger rail operations
- rail maintenance
- depot and workshop technology
- inspection, diagnostics, overhaul, reliability
- traction systems
- motors
- converters, inverters, batteries, chargers, auxiliary power, UPS
- onboard electronics
- signalling, ERTMS, ETCS, CBTC, train-control interfaces
- safety systems
- EMC, environmental testing, fire testing, shock and vibration
- EN 50121, EN 50155, EN 61373, EN 45545, or other rail standards
- testing, inspection, certification, homologation, conformity assessment
- major OEMs, suppliers, operators, infrastructure managers, and transit agencies
- Spain, Europe, USA passenger rail, Amtrak, MTA, MBTA, NJ Transit, SEPTA, WMATA, CTA, Metra, BART, Caltrain, LA Metro, Sound Transit, DART, MARTA, RTD Denver, FRA, FTA, NEC Commission, USDOT rail investment programs

OUTPUT FORMAT:
Return clean semantic HTML only. Do not include html, head, or body tags.

Use exactly this structure:

<h2>Top 20 relevant rail-sector events</h2>
<p>This section should be factual only. Do not include personalized analysis here.</p>

For each event, use this format:

<h3>1. Event title</h3>
<ul>
  <li><strong>Summary:</strong> 2 to 4 sentence general summary of what happened.</li>
  <li><strong>Source:</strong> <a href="ARTICLE_URL">Article title / publication</a></li>
  <li><strong>Region:</strong> Global / Europe / Spain / USA / China / other</li>
  <li><strong>Main category:</strong> rolling stock / infrastructure / signalling / safety / procurement / policy / supplier / maintenance / certification / other</li>
</ul>

Rules for this section:
- Include up to 20 events.
- If fewer than 20 events are genuinely relevant, include fewer than 20.
- Merge duplicate coverage into one event.
- This section must not discuss Brendan, SGS Tecnos, Erion, career implications, or personalized recommendations.
- This section must only summarize the news itself.

<h2>Global rail-sector trends</h2>
Analyze the broader global patterns suggested by the entire article set, not only the Top 20.
Use 3 to 8 concise paragraphs or bullets.
Possible trend categories include:
<ul>
  <li>fleet modernization</li>
  <li>rolling stock procurement</li>
  <li>infrastructure investment</li>
  <li>signalling and digitalization</li>
  <li>maintenance and reliability</li>
  <li>safety and regulation</li>
  <li>supplier/OEM movement</li>
  <li>testing, inspection, certification, and standards</li>
</ul>

<h2>USA passenger rail and transit trends</h2>
Analyze USA-specific patterns using the entire article set.
If there are no relevant USA items, write: "No major USA-specific trend is supported by this article set."
When relevant, discuss:
<ul>
  <li>Amtrak</li>
  <li>commuter rail</li>
  <li>urban rail / metro / light rail</li>
  <li>major transit agencies</li>
  <li>federal or state investment</li>
  <li>fleet procurement and modernization</li>
  <li>maintenance, reliability, safety, or certification implications</li>
</ul>

<h2>Potential impact on SGS Tecnos Madrid</h2>
Only include analysis supported by the article set.
If there is no realistic connection to SGS Tecnos, testing, inspection, certification, standards, lab capabilities, suppliers, or conformity assessment, write:
"No clear SGS Tecnos impact is supported by this article set."

When relevant, use this structure:
<ul>
  <li><strong>Possible impact:</strong> cautious explanation</li>
  <li><strong>Relevant article/event:</strong> article or event name</li>
  <li><strong>Possible TIC angle:</strong> testing / inspection / certification / standards / homologation / conformity assessment / supplier support</li>
  <li><strong>Standards or technical areas possibly involved:</strong> list only if reasonably inferable</li>
  <li><strong>Confidence:</strong> High / Medium / Low</li>
  <li><strong>Follow-up question:</strong> one practical question Brendan could ask internally at SGS Tecnos</li>
</ul>

Rules for this section:
- Do not invent SGS clients.
- Do not invent SGS capabilities.
- Do not claim a commercial opportunity is definite unless the article directly supports it.
- Prefer "possible relevance" and "worth watching" language.

<h2>Skills, experience, and training signals</h2>
Only include this section if the full article set supports meaningful conclusions about valuable skills, experience, or training.
If not, write:
"No clear skills or training signal is supported by this article set."

When relevant, discuss:
<ul>
  <li><strong>Most valuable technical skills:</strong></li>
  <li><strong>Most valuable hands-on experience:</strong></li>
  <li><strong>Most valuable standards/certification knowledge:</strong></li>
  <li><strong>Most valuable software, data, or documentation skills:</strong></li>
  <li><strong>Why these skills appear valuable based on this week's articles:</strong></li>
</ul>

Focus especially on:
- rolling stock maintenance
- traction systems
- onboard electronics
- signalling interfaces
- diagnostics and condition monitoring
- depot/workshop technology
- technical documentation
- requirements, verification, and validation
- rail standards and conformity assessment
- safety, reliability, and entry-into-service testing

<h2>Source list</h2>
List all articles considered in compact form. Use one line per article:
<ul>
  <li><a href="ARTICLE_URL">Article title</a> — feed/publication, date</li>
</ul>
Do not add summaries in the source list.

STYLE:
- Direct, analytical, and concise.
- Avoid hype.
- Avoid repeated summaries.
- Do not pad the report.
- Prefer clear, useful analysis over long explanation.
- Write in English.
- Preserve important Spanish technical terms when useful, such as material rodante, homologación, mantenimiento, ensayos, certificación, señalización, tracción, and taller.
"""
