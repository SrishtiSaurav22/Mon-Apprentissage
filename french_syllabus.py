from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import mm
from reportlab.lib import colors
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, HRFlowable
from reportlab.lib.enums import TA_LEFT

WIDTH, HEIGHT = A4

TEAL     = colors.HexColor("#1D9E75")
TEAL_LT  = colors.HexColor("#9FE1CB")
TEAL_DK  = colors.HexColor("#085041")
PURPLE   = colors.HexColor("#7F77DD")
PURPLE_LT= colors.HexColor("#CECBF6")
PURPLE_DK= colors.HexColor("#3C3489")
AMBER    = colors.HexColor("#BA7517")
AMBER_LT = colors.HexColor("#FAC775")
AMBER_DK = colors.HexColor("#633806")
GRAY     = colors.HexColor("#888780")
BG_LIGHT = colors.HexColor("#F7F6F3")
BORDER   = colors.HexColor("#D3D1C7")
TEXT_PRI = colors.HexColor("#1A1A18")
TEXT_SEC = colors.HexColor("#5F5E5A")
TEXT_TER = colors.HexColor("#9E9D97")
WHITE    = colors.white

doc = SimpleDocTemplate(
    "/mnt/user-data/outputs/French_DELF_A2_Syllabus_Srishti.pdf",
    pagesize=A4,
    leftMargin=18*mm, rightMargin=18*mm,
    topMargin=16*mm, bottomMargin=16*mm
)

USABLE = WIDTH - 36*mm

def S(name, **kw):
    return ParagraphStyle(name, **kw)

styles = {
    "title":       S("title",       fontName="Helvetica-Bold",    fontSize=20, textColor=TEXT_PRI, spaceAfter=2),
    "subtitle":    S("subtitle",    fontName="Helvetica",          fontSize=11, textColor=TEXT_SEC, spaceAfter=8),
    "ph_label":    S("ph_label",    fontName="Helvetica",          fontSize=10, leading=14),
    "ph_title":    S("ph_title",    fontName="Helvetica-Bold",     fontSize=12, textColor=WHITE, leading=16),
    "ph_tag":      S("ph_tag",      fontName="Helvetica",          fontSize=9,  leading=13),
    "topic_name":  S("topic_name",  fontName="Helvetica-Bold",     fontSize=10, textColor=TEXT_PRI, spaceAfter=2),
    "topic_det":   S("topic_det",   fontName="Helvetica",          fontSize=9,  textColor=TEXT_SEC, leading=14),
    "topic_time":  S("topic_time",  fontName="Helvetica-Oblique",  fontSize=8,  textColor=TEXT_TER),
    "note_title":  S("note_title",  fontName="Helvetica-Bold",     fontSize=9,  textColor=TEXT_SEC, spaceAfter=4),
    "note_body":   S("note_body",   fontName="Helvetica",          fontSize=9,  textColor=TEXT_SEC, leading=15),
    "delf_label":  S("delf_label",  fontName="Helvetica-Bold",     fontSize=10, textColor=TEXT_PRI, spaceAfter=5),
    "delf_comp":   S("delf_comp",   fontName="Helvetica-Bold",     fontSize=9,  textColor=TEXT_SEC),
    "delf_desc":   S("delf_desc",   fontName="Helvetica",          fontSize=8.5,textColor=TEXT_SEC, leading=13),
    "leg":         S("leg",         fontName="Helvetica",          fontSize=9,  textColor=TEXT_SEC),
}

story = []

# Title
story.append(Paragraph("French DELF A2 Syllabus", styles["title"]))
story.append(Paragraph("Srishti Saurav · 30 min daily · weak A2 → DELF A2 · no fixed exam date", styles["subtitle"]))
story.append(HRFlowable(width=USABLE, thickness=0.5, color=BORDER, spaceAfter=10))

# Legend
leg_items = [
    (TEAL,   "Core A2 grammar (phases 1–3)"),
    (PURPLE, "DELF exam skills (phase 4)"),
    (AMBER,  "B1 territory — after job"),
    (GRAY,   "Passive / ambient"),
]
def make_dot(col, size=8):
    t = Table([[""]], colWidths=[size], rowHeights=[size])
    t.setStyle(TableStyle([
        ("BACKGROUND",(0,0),(-1,-1), col),
        ("ROUNDEDCORNERS",[size//2]),
    ]))
    return t

leg_cells = []
for col, label in leg_items:
    inner = Table([[make_dot(col), Paragraph(label, styles["leg"])]], colWidths=[12, 88])
    inner.setStyle(TableStyle([
        ("VALIGN",(0,0),(-1,-1),"MIDDLE"),
        ("LEFTPADDING",(0,0),(-1,-1),2),
        ("RIGHTPADDING",(0,0),(-1,-1),6),
        ("TOPPADDING",(0,0),(-1,-1),1),
        ("BOTTOMPADDING",(0,0),(-1,-1),1),
    ]))
    leg_cells.append(inner)

leg_table = Table([leg_cells], colWidths=[100]*4)
leg_table.setStyle(TableStyle([
    ("LEFTPADDING",(0,0),(-1,-1),0),
    ("RIGHTPADDING",(0,0),(-1,-1),0),
    ("TOPPADDING",(0,0),(-1,-1),0),
    ("BOTTOMPADDING",(0,0),(-1,-1),0),
]))
story.append(leg_table)
story.append(Spacer(1, 10))

# DELF A2 components box
delf_comps = [
    ("Listening (CO)", "Short audio clips, everyday situations. 25 min."),
    ("Reading (CE)",   "Short texts, signs, messages, adverts. 30 min."),
    ("Writing (PE)",   "Short message, letter, or form. 45 min."),
    ("Speaking (PO)",  "Monologue + examiner interaction. 10 min."),
]
delf_cells = []
for label, desc in delf_comps:
    cell = [Paragraph(label, styles["delf_comp"]), Paragraph(desc, styles["delf_desc"])]
    delf_cells.append(cell)

delf_inner = Table(
    [[delf_cells[0], delf_cells[1]], [delf_cells[2], delf_cells[3]]],
    colWidths=[USABLE/2 - 6, USABLE/2 - 6]
)
delf_inner.setStyle(TableStyle([
    ("BACKGROUND",(0,0),(-1,-1), WHITE),
    ("BOX",(0,0),(-1,-1),0.5,BORDER),
    ("INNERGRID",(0,0),(-1,-1),0.5,BORDER),
    ("LEFTPADDING",(0,0),(-1,-1),8),
    ("RIGHTPADDING",(0,0),(-1,-1),8),
    ("TOPPADDING",(0,0),(-1,-1),6),
    ("BOTTOMPADDING",(0,0),(-1,-1),6),
    ("VALIGN",(0,0),(-1,-1),"TOP"),
    ("ROUNDEDCORNERS",[4]),
]))

delf_outer = Table(
    [[Paragraph("DELF A2 — 4 exam components (all covered in this plan)", styles["delf_label"])],
     [delf_inner]],
    colWidths=[USABLE]
)
delf_outer.setStyle(TableStyle([
    ("BACKGROUND",(0,0),(-1,-1), BG_LIGHT),
    ("BOX",(0,0),(-1,-1),0.5,BORDER),
    ("LEFTPADDING",(0,0),(-1,-1),10),
    ("RIGHTPADDING",(0,0),(-1,-1),10),
    ("TOPPADDING",(0,0),(-1,-1),8),
    ("BOTTOMPADDING",(0,0),(-1,-1),8),
    ("ROUNDEDCORNERS",[6]),
]))
story.append(delf_outer)
story.append(Spacer(1, 10))

# Phase data
phases = [
    {
        "phase": "Phase 1",
        "title": "Core verbs & present tense — the foundation",
        "tag":   "Weeks 1–3 · ~6 sessions",
        "hcol":  TEAL, "hlabel_col": TEAL_LT, "htag_col": TEAL_DK, "htag_text_col": TEAL_LT,
        "dot":   TEAL,
        "topics": [
            ("Etre & avoir",
             "All persons, auxiliary role in compound tenses — everything else builds on these two.",
             "Topic 2 · 1 session"),
            ("Le present — regular & irregular",
             "Regular -er/-ir/-re patterns, then irregular: aller, venir, faire, pouvoir, vouloir, devoir, tenir, savoir, connaitre.",
             "Topics 1, 3–9 · 3 sessions"),
            ("Il y a & verbes pronominaux",
             "Reflexive verbs (se lever, se coucher etc.) are very common in DELF A2 writing tasks.",
             "Topics 10–11 · 1 session"),
            ("Articles — definis, indefinis, partitifs",
             "All three article types with nouns. Common error zone in the writing component.",
             "Topics 38–40 · 1 session"),
        ]
    },
    {
        "phase": "Phase 2",
        "title": "Past tenses — essential for A2",
        "tag":   "Weeks 4–6 · ~6 sessions",
        "hcol":  TEAL, "hlabel_col": TEAL_LT, "htag_col": TEAL_DK, "htag_text_col": TEAL_LT,
        "dot":   TEAL,
        "topics": [
            ("Passe compose",
             "Avoir vs etre auxiliaries, agreement rules, irregular past participles — most tested past tense at A2.",
             "Topics 12, 14, 15 · 2 sessions"),
            ("Imparfait",
             "Formation + when to use vs passe compose — the contrast between the two is a classic exam question.",
             "Topic 16 · 2 sessions"),
            ("Former des questions",
             "Est-ce que, inversion, intonation — all three forms. Needed for the speaking component.",
             "Topic 13 · 1 session"),
            ("Mots interrogatifs & l'imperatif",
             "Qui, quoi, ou, quand, comment, pourquoi, combien. Imperative for instructions and requests.",
             "Topics 61, 37 · 1 session"),
        ]
    },
    {
        "phase": "Phase 3",
        "title": "Future, pronouns & connectors",
        "tag":   "Weeks 7–10 · ~8 sessions",
        "hcol":  TEAL, "hlabel_col": TEAL_LT, "htag_col": TEAL_DK, "htag_text_col": TEAL_LT,
        "dot":   TEAL,
        "topics": [
            ("Le futur simple",
             "Regular formation + irregular stems (aller→ir-, etre→ser-, avoir→aur- etc.).",
             "Topics 17–18 · 2 sessions"),
            ("Pronouns — COD, COI, y, en, ordre",
             "Learn in sequence: subjects → COD → COI → y → en → order. Heavily tested in reading and writing.",
             "Topics 43–48 · 3 sessions"),
            ("Adjectifs possessifs & comparaisons",
             "Mon/ma/mes etc., plus/moins/aussi...que comparisons. Topics 50–52.",
             "1 session"),
            ("Connecteurs & adverbes de temps",
             "Parce que, donc, mais, puis, ensuite, enfin — essential for writing a coherent short text.",
             "Topics 60, 69–71 · 2 sessions"),
        ]
    },
    {
        "phase": "Phase 4",
        "title": "DELF A2 exam skills — all 4 components",
        "tag":   "Weeks 11–14 · ongoing",
        "hcol":  PURPLE, "hlabel_col": PURPLE_LT, "htag_col": PURPLE_DK, "htag_text_col": PURPLE_LT,
        "dot":   PURPLE,
        "topics": [
            ("Comprehension orale (listening)",
             "RFI Journal en francais facile, TV5Monde A2 exercises. Focus: gist + specific info from everyday dialogues.",
             "2x per week · 15 min each"),
            ("Comprehension ecrite (reading)",
             "RFI Savoirs, DELF A2 past papers. Practice scanning short notices, messages, and adverts.",
             "2x per week · 15 min each"),
            ("Production ecrite (writing)",
             "Short messages, emails, postcards using grammar from phases 1–3. Le Petit Prince as model sentences.",
             "1x per week · 30 min"),
            ("Production orale (speaking)",
             "Record yourself for 2 min on everyday topics (ma journee, mes projets, mon quartier). Songs help with intonation.",
             "1x per week · 20 min"),
        ]
    },
    {
        "phase": "Phase 5",
        "title": "B1 territory — after you have a job",
        "tag":   "Not now",
        "hcol":  AMBER, "hlabel_col": AMBER_LT, "htag_col": AMBER_DK, "htag_text_col": AMBER_LT,
        "dot":   AMBER,
        "topics": [
            ("Conditionnel present & subjonctif",
             "Topics 22–26 — important but B1 level. Don't study these before passe compose and futur are solid.",
             ""),
            ("Plus-que-parfait, futur anterieur, passe simple",
             "Topics 19, 21, 33 — passe simple appears in L'Etranger but is not tested at A2 at all.",
             ""),
            ("Discours indirect, voix passive, concordance des temps",
             "Topics 34–36 — solidly B1/B2. Dissertation, nominalisation, these-antithese-synthese (66–68) are B2 academic writing.",
             ""),
            ("Pronoms relatifs complexes & pronoms composes",
             "Topics 55–59 (lequel/laquelle, ce dont, ce a quoi) — useful eventually, not A2 requirements.",
             ""),
        ]
    },
]

def build_phase(phase):
    hcol     = phase["hcol"]
    dot_col  = phase["dot"]
    lbl_col  = phase["hlabel_col"]
    tag_col  = phase["htag_col"]
    tag_tc   = phase["htag_text_col"]

    ph_label_s = ParagraphStyle("phl", fontName="Helvetica", fontSize=10, textColor=lbl_col, leading=14)
    ph_title_s = ParagraphStyle("pht", fontName="Helvetica-Bold", fontSize=12, textColor=WHITE, leading=16)
    ph_tag_s   = ParagraphStyle("phtag", fontName="Helvetica", fontSize=9, textColor=tag_tc, leading=13)

    header_inner = Table(
        [[Paragraph(phase["phase"], ph_label_s),
          Paragraph(phase["title"], ph_title_s),
          Paragraph(phase["tag"], ph_tag_s)]],
        colWidths=[50, USABLE - 130, 80]
    )
    header_inner.setStyle(TableStyle([
        ("VALIGN",(0,0),(-1,-1),"MIDDLE"),
        ("ALIGN",(2,0),(2,0),"RIGHT"),
        ("LEFTPADDING",(0,0),(-1,-1),0),
        ("RIGHTPADDING",(0,0),(-1,-1),0),
        ("TOPPADDING",(0,0),(-1,-1),0),
        ("BOTTOMPADDING",(0,0),(-1,-1),0),
    ]))
    header_table = Table([[header_inner]], colWidths=[USABLE])
    header_table.setStyle(TableStyle([
        ("BACKGROUND",(0,0),(-1,-1), hcol),
        ("LEFTPADDING",(0,0),(-1,-1),10),
        ("RIGHTPADDING",(0,0),(-1,-1),10),
        ("TOPPADDING",(0,0),(-1,-1),8),
        ("BOTTOMPADDING",(0,0),(-1,-1),8),
        ("ROUNDEDCORNERS",[6,6,0,0]),
    ]))

    topic_rows = []
    for i, (name, detail, time) in enumerate(phase["topics"]):
        content = [Paragraph(name, styles["topic_name"]), Paragraph(detail, styles["topic_det"])]
        if time:
            content.append(Paragraph(time, styles["topic_time"]))

        dot = make_dot(dot_col, 7)
        row_t = Table([[dot, content]], colWidths=[13, USABLE - 26])
        row_t.setStyle(TableStyle([
            ("VALIGN",(0,0),(0,0),"TOP"),
            ("TOPPADDING",(0,0),(0,0),3),
            ("LEFTPADDING",(0,0),(-1,-1),0),
            ("RIGHTPADDING",(0,0),(-1,-1),0),
            ("TOPPADDING",(0,1),(1,0),0),
            ("BOTTOMPADDING",(0,0),(-1,-1),0),
        ]))
        topic_rows.append([row_t])
        if i < len(phase["topics"]) - 1:
            topic_rows.append([HRFlowable(width=USABLE - 20, thickness=0.5, color=BORDER)])

    body_table = Table(topic_rows, colWidths=[USABLE])
    body_table.setStyle(TableStyle([
        ("BACKGROUND",(0,0),(-1,-1), WHITE),
        ("LEFTPADDING",(0,0),(-1,-1),10),
        ("RIGHTPADDING",(0,0),(-1,-1),10),
        ("TOPPADDING",(0,0),(-1,-1),7),
        ("BOTTOMPADDING",(0,0),(-1,-1),7),
        ("BOX",(0,0),(-1,-1),0.5,BORDER),
        ("ROUNDEDCORNERS",[0,0,6,6]),
    ]))

    outer = Table([[header_table],[body_table]], colWidths=[USABLE])
    outer.setStyle(TableStyle([
        ("LEFTPADDING",(0,0),(-1,-1),0),
        ("RIGHTPADDING",(0,0),(-1,-1),0),
        ("TOPPADDING",(0,0),(-1,-1),0),
        ("BOTTOMPADDING",(0,0),(-1,-1),0),
    ]))
    return outer

# Ambient phase (gray header)
def build_ambient():
    ph_label_s = ParagraphStyle("amb_lbl", fontName="Helvetica-Bold", fontSize=10, textColor=TEXT_SEC, leading=14)
    ph_title_s = ParagraphStyle("amb_tit", fontName="Helvetica-Bold", fontSize=12, textColor=TEXT_PRI, leading=16)
    ph_tag_s   = ParagraphStyle("amb_tag", fontName="Helvetica", fontSize=9, textColor=TEXT_SEC, leading=13)

    header_inner = Table(
        [[Paragraph("Ambient", ph_label_s),
          Paragraph("Passive learning — no sessions needed", ph_title_s),
          Paragraph("ongoing", ph_tag_s)]],
        colWidths=[55, USABLE - 125, 70]
    )
    header_inner.setStyle(TableStyle([
        ("VALIGN",(0,0),(-1,-1),"MIDDLE"),
        ("ALIGN",(2,0),(2,0),"RIGHT"),
        ("LEFTPADDING",(0,0),(-1,-1),0),("RIGHTPADDING",(0,0),(-1,-1),0),
        ("TOPPADDING",(0,0),(-1,-1),0),("BOTTOMPADDING",(0,0),(-1,-1),0),
    ]))
    header_table = Table([[header_inner]], colWidths=[USABLE])
    header_table.setStyle(TableStyle([
        ("BACKGROUND",(0,0),(-1,-1), BG_LIGHT),
        ("BOX",(0,0),(-1,-1),0.5,BORDER),
        ("LEFTPADDING",(0,0),(-1,-1),10),("RIGHTPADDING",(0,0),(-1,-1),10),
        ("TOPPADDING",(0,0),(-1,-1),8),("BOTTOMPADDING",(0,0),(-1,-1),8),
        ("ROUNDEDCORNERS",[6,6,0,0]),
    ]))

    amb_topics = [
        ("French songs", "Keep listening. Intonation, rhythm, vocabulary absorption without effort. Don't annotate — just listen."),
        ("Le Petit Prince", "Read when you feel like it, not as a task. Clean, simple French — better input than any textbook exercise."),
        ("RFI Savoirs", "When you open it, it counts as your French for the day. Don't combine with a grammar session on the same day."),
    ]
    topic_rows = []
    for i, (name, detail) in enumerate(amb_topics):
        content = [Paragraph(name, styles["topic_name"]), Paragraph(detail, styles["topic_det"])]
        dot = make_dot(GRAY, 7)
        row_t = Table([[dot, content]], colWidths=[13, USABLE - 26])
        row_t.setStyle(TableStyle([
            ("VALIGN",(0,0),(0,0),"TOP"),("TOPPADDING",(0,0),(0,0),3),
            ("LEFTPADDING",(0,0),(-1,-1),0),("RIGHTPADDING",(0,0),(-1,-1),0),
            ("TOPPADDING",(0,1),(1,0),0),("BOTTOMPADDING",(0,0),(-1,-1),0),
        ]))
        topic_rows.append([row_t])
        if i < len(amb_topics) - 1:
            topic_rows.append([HRFlowable(width=USABLE-20, thickness=0.5, color=BORDER)])

    body_table = Table(topic_rows, colWidths=[USABLE])
    body_table.setStyle(TableStyle([
        ("BACKGROUND",(0,0),(-1,-1), WHITE),
        ("LEFTPADDING",(0,0),(-1,-1),10),("RIGHTPADDING",(0,0),(-1,-1),10),
        ("TOPPADDING",(0,0),(-1,-1),7),("BOTTOMPADDING",(0,0),(-1,-1),7),
        ("BOX",(0,0),(-1,-1),0.5,BORDER),
        ("ROUNDEDCORNERS",[0,0,6,6]),
    ]))
    outer = Table([[header_table],[body_table]], colWidths=[USABLE])
    outer.setStyle(TableStyle([
        ("LEFTPADDING",(0,0),(-1,-1),0),("RIGHTPADDING",(0,0),(-1,-1),0),
        ("TOPPADDING",(0,0),(-1,-1),0),("BOTTOMPADDING",(0,0),(-1,-1),0),
    ]))
    return outer

for phase in phases:
    story.append(build_phase(phase))
    story.append(Spacer(1, 9))

story.append(build_ambient())
story.append(Spacer(1, 9))

# Daily 30 min note
note_table = Table(
    [[Paragraph("How to use the 30 min daily", styles["note_title"])],
     [Paragraph(
        "Phases 1–3: one grammar topic per session. Learn the rule (5 min) → workbook exercises (15 min) → write 3–5 original sentences (10 min).<br/>"
        "Phase 4: rotate the 4 exam components across the week — don't try to do all four in one sitting.<br/>"
        "Minimum viable day: open the workbook, do one exercise. That's enough to keep the streak alive.",
        styles["note_body"]
     )]],
    colWidths=[USABLE]
)
note_table.setStyle(TableStyle([
    ("BACKGROUND",(0,0),(-1,-1), BG_LIGHT),
    ("BOX",(0,0),(-1,-1),0.5,BORDER),
    ("LEFTPADDING",(0,0),(-1,-1),10),("RIGHTPADDING",(0,0),(-1,-1),10),
    ("TOPPADDING",(0,0),(-1,-1),8),("BOTTOMPADDING",(0,0),(-1,-1),8),
    ("ROUNDEDCORNERS",[6]),
]))
story.append(note_table)

doc.build(story)
print("Done.")
