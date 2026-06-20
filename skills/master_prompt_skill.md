# Skill: Master Content & Design Integration

## Metadata
- **File**: `skills/master_prompt_skill.md`
- **Purpose**: Combines both LinkedIn high-engaging copy and complete Canva/Visual Design specifications into a unified, synchronized marketing package.
- **When to invoke**: User requests a complete social media package, high-impact content WITH visual design specs, integrated brand marketing materials, or visual posts for LinkedIn/Instagram.

---

## Input Parameters
The following parameters are used to configure the integrated package. Bold parameters are **required**.

| Parameter | Type | Required | Default | Description |
| :--- | :--- | :--- | :--- | :--- |
| **`topic`** | String | **Yes** | - | The main subject or message of the post. |
| **`audience`** | String | **Yes** | - | Target reader/viewer demographic (e.g., developers, VCs, HR managers). |
| **`brand_name`** | String | **Yes** | - | Name of the company or brand. |
| **`industry`** | String | **Yes** | - | Industry sector (e.g., `tech`, `real estate`, `wellness`, `retail`). |
| `tone_preference` | String | No | `"professional"` | The style/tone override for the copy (e.g., `casual`, `inspirational`). |
| `goal` | String | No | `"engagement"` | The objective of the campaign (e.g., `lead generation`, `brand awareness`). |
| `preferences` | String | No | `"minimalist"`| Creative aesthetic for the design (e.g., `minimalist`, `bold`, `playful`). |
| **`deliverable`** | String | **Yes** | - | The visual format (e.g., `LinkedIn single post + graphic`, `Canva Presentation`). |

---

## Skill Instructions & Guidelines

When this skill is invoked, act as both a **Lead Copywriter** and an **Art Director** collaborating on a high-converting digital campaign. You must ensure that the written copy and the visual design are fully synchronized and reinforce each other.

### Step 1: Design the Strategy
Understand the synergy between text and visual. For example, if the graphic uses high-contrast bold typography with a minimalist background, the LinkedIn copy should start with a bold statement hook that matches the exact text on the graphic.

### Step 2: Write the Content (Part 1)
- Refer to `skills/linkedin_post_skill.md` guidelines.
- Generate three hooks, select the recommended one with a rationale, and write the full high-engagement post.
- Ensure the copy transitions smoothly from an audience problem to your topic's solution, ending in a strong, goal-oriented CTA.
- Provide 3-7 hashtags.

### Step 3: Architect the Design Specifications (Part 2)
- Refer to `skills/design_optimization_skill.md` guidelines.
- Establish visual brand guidelines, typography hierarchy (using Canva-friendly fonts), a custom color palette table, and layout grid blueprints.
- Deliver step-by-step Canva templates, shortcuts, elements, and export directions.

### Step 4: Synchronize and Integrate (Part 3)
- Bridge the gap between copy and graphic. Detail exactly:
  - **Graphic Copy**: What exact text/words should be written *on* the image or first page of the carousel (usually the recommended hook or a shortened, high-impact version of it).
  - **Visual-Content Alignment**: How the graphic's layout reflects the post's structure (e.g., "The graphic displays a 3-step checklist, corresponding directly to the 3 main bullet points in Section 2 of the LinkedIn copy").
  - **Campaign Integration workflow**: Provide a timeline or concrete next steps on how to build, publish, and monitor this post + graphic package for maximum reach.

---

## Output Template

Your output MUST strictly follow this Markdown structure:

```markdown
# Master Content & Design Campaign Package

## Executive Summary
* **Topic**: [Topic]
* **Brand & Industry**: [Brand Name] | [Industry]
* **Audience**: [Audience]
* **Aesthetic & Tone**: [Preferences] | [Tone Preference]
* **Goal & Deliverable**: [Goal] | [Deliverable]

---

## PART 1: LinkedIn Content Package (Copywriting)

### 1. Hook Strategy
* **Option A (Question)**: [Text]
* **Option B (Statistic/Fact)**: [Text]
* **Option C (Bold Statement)**: [Text]

**Recommended Hook**: [Option A/B/C]
**Rationale**: [Why this hook matches the brand, audience, and deliverable format]

### 2. Full LinkedIn Post Content
[Recommended Hook]

[High-readability body copy, with single-sentence lines, spacing, and structured storytelling (Problem -> Agitate -> Solve)]

[Goal-oriented CTA]

.
.
.
[3-7 Hashtags]

---

## PART 2: Design Specifications & Canva Workflow (Visuals)

### 1. Visual Theme & Brand Guidelines
* **Brand Aesthetic**: [Define style]
* **Design Guidelines**: [Core rules for this design]

### 2. Typographic Pairings (Canva)
| Role | Recommended Font | Suggested Sizing / Weight | Purpose |
| :--- | :--- | :--- | :--- |
| **Title / Hero** | [Font Name] | Bold, [Size] | Text on graphic (Title) |
| **Subtitle** | [Font Name] | Regular/Italic, [Size] | Underline text/tagline on graphic |
| **Accent Elements** | [Font Name] | Medium, [Size] | Category badges, metrics, calls-to-action |

### 3. Campaign Color Palette
| Color Role | Color Name | HEX Code | Distribution | Best Used For |
| :--- | :--- | :--- | :--- | :--- |
| Dominant (60%) | [Name] | `#[HEX]` | 60% | Background / Main panels |
| Secondary (30%)| [Name] | `#[HEX]` | 30% | Key Text / Symmetrical framing |
| Accent (10%) | [Name] | `#[HEX]` | 10% | CTA highlights / Metric badges / Icons |

### 4. Layout & Placement Blueprint
* **Visual Grid**: [Describe placement of text, icons, and shapes on the canvas]
* **Focal Element**: [The primary visual anchor]
* **Negative Space Rule**: [How to preserve breathing room]

### 5. Canva Workflow & Optimization
* **Canva Element Search Terms**: `"[Term 1]"`, `"[Term 2]"`
* **Canva Shortcut Cheatsheet**:
  * [Shortcut 1]
  * [Shortcut 2]
* **Recommended Canvas Size**: `[e.g., 1080 x 1350 px (Portrait)]`
* **High-DPI Export Settings**: [Format, resolution multiplier, and options]

---

## PART 3: Content-Visual Integration & Execution Guide

### 1. Text Overlay Specifications (What to put ON the graphic)
* **Main Heading on Graphic**: "[Exact wording for the main text on the Canva visual]"
* **Sub-Heading / Supporting Text**: "[Exact wording for the sub-text or secondary highlight on the graphic]"
* **CTA Button on Graphic**: "[e.g., 'Swipe for more' or 'Link in bio icon']"

### 2. Visual-Content Synergy
* **Alignment Rationale**: [Explain how the design elements reinforce the copy, e.g., "The dark charcoal background reinforces the serious 'emergency' tone of the post, while the neon green accent highlights the 'immediate action' required in the copy."]
* **User Engagement Hook**: [e.g., "The graphic contains a 'Page 1 of 5' marker prompting the user to swipe, while the post copy mentions 'See the visual checklist in the carousel'."]

### 3. Immediate Next Steps / Launch Checklist
1. **Canva Setup**: Open Canva, create a custom size of `[Size]`, and insert the custom color HEX codes.
2. **Visual Production**: Apply the grid blueprint, use typographic hierarchy, and overlay the exact text specified in Section 1 of Part 3. Export as PNG.
3. **LinkedIn Scheduling**: Copy the text from Part 1. Upload the exported PNG/PDF graphic first, paste the caption text, and pin the 'First Comment' under the post immediately after publishing.
4. **Active Engagement**: Monitor and reply to every comment within the first 60 minutes using the 'Interaction Prompt' strategy.
```

