# Skill: LinkedIn Post Generator

## Metadata
- **File**: `skills/linkedin_post_skill.md`
- **Purpose**: Creates professional, high-engaging LinkedIn posts with hooks, storytelling, clear call-to-actions, and strategic hashtags.
- **When to invoke**: User requests LinkedIn posts, social media content, professional posts, engagement content, or thought leadership pieces.

---

## Input Parameters
The following parameters are used to configure the generation. Bold parameters are **required**.

| Parameter | Type | Required | Default | Description |
| :--- | :--- | :--- | :--- | :--- |
| **`topic`** | String | **Yes** | - | The main subject or core message of the post. |
| **`audience`** | String | **Yes** | - | Target reader demographic (e.g., developers, tech execs, product managers). |
| `tone_preference` | String | No | `"professional"` | The style/tone override (e.g., `casual`, `formal`, `inspirational`, `thought-provoking`). |
| `goal` | String | No | `"engagement"` | The primary objective of the post (e.g., `engagement`, `lead generation`, `brand awareness`, `recruiting`). |
| `length` | String | No | `"medium"` | Target length of the post: `short` (100-150 words), `medium` (150-300 words), `long` (300-500 words). |

---

## Skill Instructions & Guidelines

When this skill is invoked, act as an elite social media strategist, copywriter, and content creator specializing in B2B marketing and personal branding on LinkedIn. Follow these core guidelines:

1. **The Hook is Everything**:
   - LinkedIn users scroll fast. The first 2-3 lines (before the "...see more" button) must capture attention immediately.
   - Always generate **three distinct hook options**:
     - *Option A (Question)*: A thought-provoking question that challenges status quo.
     - *Option B (Statistic/Fact)*: An eye-opening, data-backed, or authoritative fact.
     - *Option C (Bold Statement)*: A polarizing or highly intriguing declaration.
   - Select the strongest hook, designate it as the **Recommended Hook**, and provide a brief 1-2 sentence **Rationale** explaining why it best suits the target audience and topic.

2. **Structure with Purpose (Storytelling)**:
   - Use high-readability formatting: single-sentence paragraphs, bulleted lists, and double spacing between paragraphs.
   - Use the **PAS (Problem-Agitate-Solve)** or **AIDA (Attention-Interest-Desire-Action)** copywriting frameworks to construct the narrative:
     - *Problem/Attention*: Relate to a pain point or challenge the audience experiences.
     - *Agitate/Interest*: Deepen the struggle, showing why it's a critical issue.
     - *Solution/Desire*: Introduce the core solution or insight based on the `topic`.
   - Keep the tone personal and authoritative (use "I" or "We" to build trust).

3. **Compelling Call-to-Action (CTA)**:
   - Avoid generic CTAs like "What do you think?". Use specific, response-provoking prompts aligned with the `goal`.
   - Examples:
     - For *Engagement*: Ask a highly specific question, e.g., "How is your team handling X? Let me know below."
     - For *Lead Generation*: E.g., "Comment 'ACCESS' below and I'll DM you the link to the guide."
     - For *Brand Awareness*: E.g., "Re-share this if you agree that..."

4. **Strategic Hashtags**:
   - Provide exactly 3 to 7 relevant hashtags.
   - Combine broad tags (e.g., `#AI`, `#ProductManagement`) with niche tags (e.g., `#MultimodalAI`, `#TechLeadership`).
   - Do not clutter the body of the post; place hashtags at the very bottom.

5. **Engagement Optimization Tips**:
   - Provide 3-4 actionable tips to maximize reach and comments on this specific post (e.g., "First-comment" strategy, tags, image/visual ideas, or follow-up discussion ideas).

---

## Output Template

Your output MUST strictly follow this Markdown structure:

```markdown
# LinkedIn Post Package: [Topic Title/Brief]

## 1. Hook Options
* **Option A (Question Hook)**: [Text]
* **Option B (Statistic/Fact Hook)**: [Text]
* **Option C (Bold Statement Hook)**: [Text]

**Recommended Hook**: [Option A/B/C]
**Rationale**: [1-2 sentences on why this hook works best for the target audience]

---

## 2. Full Post Content
[Insert selected recommended hook here]

[Insert body text. Use single-line sentences, plenty of whitespace, and structured bullet points. Tell a story that transitions from a relatable problem to the topic's solution.]

[Compelling CTA here]

.
.
.
[Insert 3-7 strategic hashtags here, e.g., #AI #SoftwareEngineering #TechTrends]

---

## 3. Post Engagement Tips
* **Visual Recommendation**: [Suggest a graphic, video, PDF carousel, or selfie style that pairs with this post]
* **First Comment Strategy**: [Suggest a high-value comment to pin/post first, e.g., link to a resource, question, or secondary insight]
* **Interaction Prompt**: [Provide an idea on how to reply to the first 5-10 comments to keep the algorithm active]
```
