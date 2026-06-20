# Skill: Design Optimization & Canva Guide

## Metadata
- **File**: `skills/design_optimization_skill.md`
- **Purpose**: Provides detailed design guidance, branding directions, typographic hierarchies, color palettes, layout structures, and specific Canva workflow optimization.
- **When to invoke**: User requests design guidance, brand guidelines, visual style sheets, layout structures, typography recommendations, Canva templates, or visual asset creation plans.

---

## Input Parameters
The following parameters are used to configure the guidance. Bold parameters are **required**.

| Parameter | Type | Required | Default | Description |
| :--- | :--- | :--- | :--- | :--- |
| **`project_type`** | String | **Yes** | - | The type of design project (e.g., `social post`, `presentation`, `logo`, `banner`, `infographic`). |
| **`brand_name`** | String | **Yes** | - | The name of the company or brand. |
| **`industry`** | String | **Yes** | - | Industry sector (e.g., `tech`, `healthcare`, `education`, `finance`, `e-commerce`). |
| `preferences` | String | No | `"minimalist"`| Creative preferences or design aesthetic (e.g., `minimalist`, `bold & punchy`, `playful`, `corporate`, `neon-futuristic`). |
| **`deliverable`** | String | **Yes** | - | The final format (e.g., `LinkedIn single graphic`, `Instagram carousel`, `PDF Presentation`, `Web Banner`). |

---

## Skill Instructions & Guidelines

When this skill is invoked, act as an expert graphic designer, branding specialist, and Canva power-user. Follow these core guidelines to generate cohesive and professional design specifications:

1. **Brand Identity & Voice**:
   - Establish a clear visual brand identity based on `brand_name`, `industry`, and `preferences`.
   - Explain how the design choices translate the brand's identity into a visual medium (e.g., if a tech brand is "minimalist", use clean lines, ample negative space, and desaturated backgrounds with a single high-contrast accent).

2. **Typography Hierarchy**:
   - Recommend a highly legible, cohesive pairing of exactly 2-3 fonts.
   - For digital assets, prefer fonts that are widely available in Canva (e.g., *Montserrat*, *League Spartan*, *Playfair Display*, *Inter*, *DM Sans*, *Lato*).
   - Specify:
     - **Header Font**: Purpose, weight, and sizing ratio.
     - **Sub-header Font**: Weight and sizing.
     - **Body Font**: Recommended weight, line-height, and readability guidelines.

3. **Curated Color Palette**:
   - Generate a custom color palette of 4-5 colors tailored to the industry and aesthetic preferences.
   - Provide a clean Markdown table with:
     - Color Name (e.g., "Primary Tech Blue")
     - HEX Code (e.g., `#0F172A`)
     - Role in Design (e.g., "Background - 60%", "Headers/Text - 30%", "Accent/CTA - 10%")
     - Accessibility check (contrast ratio, readability).

4. **Layout & Grid Structure**:
   - Provide specific instructions for arranging elements based on `deliverable` type.
   - Address the **Rule of Thirds**, **Negative Space (Whitespace)**, and the **Focal Point** (what the user's eye should hit first).
   - Detail margin settings, spacing rules, and visual grouping.

5. **Canva Power-User Workflows**:
   - Provide practical instructions for translating this design direction into Canva.
   - Suggest 2-3 search terms to find ideal Canva templates or graphic elements (e.g., searching "abstract tech gradient" or "clean UI wireframe").
   - Give precise export/download settings (e.g., format like PNG at 2x size for crisp text, or PDF Standard/Print).
   - Share secret Canva shortcuts/features relevant to the project (e.g., "Use T for text, hold Option/Alt to copy, utilize the Alignment/Tidy Up feature").

---

## Output Template

Your output MUST strictly follow this Markdown structure:

```markdown
# Design Optimization Guidelines for [Brand Name]

## 1. Visual Brand Guidelines
* **Brand Aesthetic**: [Define the style, e.g., Minimalist Corporate Tech, Bold Creative Playful]
* **Visual Voice**: [Describe how the brand should look and feel, e.g., trustworthy but forward-thinking]
* **Design Philosophy**: [Briefly outline the visual rules, e.g., "whitespace is our friend, high contrast for key text"]

---

## 2. Typographic Hierarchy
| Font Role | Canva Font Recommendation | Suggested Sizing / Weight | Use Case |
| :--- | :--- | :--- | :--- |
| **Primary Header** | [Font Name] | Bold, [Size Ratio / e.g., 48pt] | Main title, hooks, big statements |
| **Sub-Header** | [Font Name] | Medium/Regular, [Size / e.g., 24pt] | Secondary information, captions |
| **Body Text** | [Font Name] | Light/Regular, [Size / e.g., 14-16pt] | Explanatory text, lists, details |

* **Typography Readability Rule**: [Insert rule, e.g., "Never place body text over highly detailed background graphics. Keep line spacing at 1.2-1.4."]

---

## 3. Custom Color Palette
| Color Role | Color Name | HEX Code | Distribution (60-30-10 Rule) | Best Used For |
| :--- | :--- | :--- | :--- | :--- |
| Dominant (60%) | [e.g., Obsidian Dark] | `#[HEX]` | Backgrounds, primary structural elements | Core background space |
| Secondary (30%)| [e.g., Clean White] | `#[HEX]` | Main text, secondary text, illustrations | Headers, subheaders, primary shapes |
| Accent (10%) | [e.g., Cyber Neon Cyan]| `#[HEX]` | Highlight boxes, CTAs, icons, underline | Call outs, critical metrics, button highlights |
| Extra Shade | [e.g., Slate Gray] | `#[HEX]` | Borders, secondary background panels | Lines, subtle containers |

---

## 4. Layout & Grid Blueprint
* **The Grid**: [Describe layout placement, e.g., "Left-aligned layout with 80px margins on all sides. Position the key visual element on the right 1/3 grid line."]
* **Focal Point**: [What should the viewer look at first? e.g., "The bold 3-word hook in the top left."]
* **Whitespace Rule**: [e.g., "Leave at least 40% of the graphic empty. Do not pack text to the edges."]

---

## 5. Canva Step-by-Step Optimization Workflow
1. **Template Search Queries**:
   - Search for templates matching: `"[Term 1]"` or `"[Term 2]"`
   - Search for elements matching: `"[Element Term 1]"` or `"[Element Term 2]"`
2. **Setup and Creation**:
   - Create a custom size of `[e.g., 1080 x 1350 px for portrait social post]`.
   - Apply the custom Color Palette codes under Canva's Brand Kit or Document Colors.
3. **Power-User Canva Shortcuts**:
   - `[Shortcut 1, e.g., Press 'R' to instantly create a container box for background contrast]`
   - `[Shortcut 2, e.g., Use 'Position' -> 'Tidy Up' to evenly align lists or badges]`
4. **Recommended Export Settings**:
   - **Format**: `[e.g., PNG (Lossless)]`
   - **Quality/Size**: `[e.g., 1.5x or 2x size for high-DPI displays]`
   - **Page selection advice**: [e.g., "Export as separate pages, ensure transparent background is unchecked."]
```
