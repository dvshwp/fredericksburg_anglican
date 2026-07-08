# Managing the Church Website — A Plain-English Guide

*For whoever looks after the website. No technical background needed. If you can
fill in a form and click a button, you can do everything in this guide.*

---

## The big picture (read this once)

Your website is just a small set of **files** (the pages, the styling, and the
images). Those files live in a free service called **GitHub**. GitHub also does
the job of a **web host** — it shows those files to the world at your web
address, `https://fredericksburganglican.org`, at no cost.

So there are only ever two ideas to hold in your head:

1. **To change the website, you change a file.**
2. **After you change a file, you click a button called "Commit" to publish it.**

That's the whole job. The rest of this guide is just the specific buttons to
click for the specific things you'll want to change.

You will do almost everything from the GitHub website in a normal web browser —
**no special software to install.**

> **One golden rule:** you can only break the site by changing things you weren't
> meant to. When editing, only change the words, and leave the little `<angle
> bracket>` tags alone. If in doubt, don't save — just close the tab. Nothing
> changes until you click "Commit."

---

## Part 1 — The task you'll do most often: posting the next event

Your church posts its "next gathering" in **two places that must match**:

- **A picture** — the tall announcement graphic (`next_event.png`).
- **Four lines of text** — so Google and phone assistants can actually read the
  date, time, and place (they can't read words inside a picture).

Updating an event means updating both. It takes about five minutes.

### Step 1 — Get your new announcement picture ready

- Make your announcement graphic **tall and narrow** (portrait), about the same
  shape as a sheet of paper standing up (a 5-to-7 ratio).
- Save it as a **PNG** file, and name it **exactly**: `next_event.png`
  (all lowercase, with the underscore, no spaces).
- Try to keep the file **under a few hundred KB** so the page loads fast on
  phones. (Most graphics apps have an "export" or "compress" option.)

### Step 2 — Replace the picture on GitHub

1. Go to your repository on **github.com** (the page listing all your files).
2. Click into the **`images`** folder.
3. Click the old **`next_event.png`** to open it, then look for a **trash/bin
   icon** to delete it, and **Commit** that deletion. *(Deleting first avoids any
   name mix-ups.)*
4. Go back into the **`images`** folder. Click **"Add file" → "Upload files."**
5. Drag in your new `next_event.png` and click **"Commit changes."**

> The filename must stay **`next_event.png`** every time. That is the secret that
> lets you swap the picture without touching any code.

### Step 3 — Update the four lines of text

1. In your repository, click **`index.html`** to open it.
2. Click the **pencil icon (✏️)** at the top right to edit it.
3. Press **Ctrl+F** (Windows) or **Cmd+F** (Mac) and search for:
   **`Our next gathering`**
4. Just below that you'll see four lines wrapped by arrow comments
   (`↓↓↓ EDIT THESE FOUR LINES ↓↓↓`). They look like this:

   ```
   <p><span class="label">What:</span> [WHAT, e.g. Sunday Worship & Holy Communion]</p>
   <p><span class="label">Date:</span> [DATE, e.g. Sunday, September 14, 2025]</p>
   <p><span class="label">Time:</span> [TIME, e.g. 10:00 AM]</p>
   <p><span class="label">Location:</span> [VENUE NAME], [STREET ADDRESS], Fredericksburg, VA [ZIP]</p>
   ```

5. **Type your real details over the parts in [square brackets] only.** Leave
   everything else on the line exactly as it is. Finished, a line looks like:

   ```
   <p><span class="label">Date:</span> Sunday, September 14, 2025</p>
   ```

   *(Tiny detail: if you need an "&" symbol in the text, write it as `&amp;`.
   That's just how web pages spell an ampersand.)*

6. Scroll up and click the green **"Commit changes…"** button, then confirm.

### Step 4 — Check it

Wait about a minute, then open `https://fredericksburganglican.org` and refresh.
Your new picture and text should be there. Done!

You do **not** need to edit the Events page for this — it automatically points to
the details you just entered on the home page.

---

## Part 2 — Other things you might change (less often)

All of these are edited the same way: open the file, click the **pencil (✏️)**,
change the words, click **"Commit changes."**

| What you want to change | File to open | Search for… |
|---|---|---|
| List of upcoming events ("On the calendar") | `events.html` | `On the calendar` |
| The "Give" button's link | `index.html` | `qgiv.com` |
| Contact email address | `index.html` | `CONTACT_EMAIL_HERE` |
| Welcome wording / service info | `index.html` | the words you want to change |
| Church name in a couple of spots | `index.html` | `[CHURCH NAME]` |

**Adding calendar events:** in `events.html`, find `On the calendar`. You'll see
lines like:

```
<li>[DATE] — [EVENT NAME]: [ONE-LINE DESCRIPTION]</li>
```

Type your event over the placeholder text, keeping the `<li>` at the start and
`</li>` at the end. To add another event, copy a whole `<li>…</li>` line and paste
it below. To remove one, delete a whole `<li>…</li>` line.

---

## Part 3 — What "Commit" and "publish" mean

Every time you click **"Commit changes,"** GitHub saves your edit *and*
republishes the website with that change. There is no separate "publish" button —
committing is publishing. GitHub also asks for a short note ("commit message")
like *"Update event for September 14"* — this is just a diary entry so you can
remember what you changed. Write anything helpful; it doesn't affect the site.

---

## Part 4 — The short list of things NOT to do

- **Don't rename files or folders** (`index.html`, `events.html`, `images/`,
  `css/`, and the filename `next_event.png` must stay exactly as they are).
- **Don't delete the `<angle-bracket>` tags** when editing — only change the
  words between them.
- **Don't add a file named `.nojekyll`** — it would change how GitHub serves the
  site and could expose the internal guide files described at the end.
- **Don't touch the `css/` folder** unless you're intentionally changing colors
  or fonts (instructions for that are in the main `README.md`).

---

## Part 5 — If something looks wrong

Nothing you do here is permanent — GitHub keeps a full history of every change.

- **To undo your last change:** on github.com, open the file, click the **"History"**
  link, find the previous version, and you can revert to it. (Or simply edit the
  file again and fix the text.)
- **If the whole site looks broken** after an edit, you most likely changed or
  deleted a `<tag>` by accident. Reverting to the previous version from History
  fixes it.
- **When in doubt, ask the person who set this up.** Bring them the web address
  and describe what you clicked — that's usually enough to sort it out quickly.

---

## Mini-glossary (the scary words, in plain English)

- **Repository (or "repo")** — the folder on GitHub that holds all your website
  files.
- **GitHub** — the free service that both stores your files and shows them to the
  world as a website.
- **GitHub Pages** — the specific GitHub feature that turns your files into a live
  website.
- **Commit** — clicking "save & publish" on GitHub. It records your change and
  updates the live site.
- **HTML** — the kind of file a web page is written in (`index.html`). It's plain
  text with `<tags>` that tell the browser how to show things.
- **Tag** — the little `<…>` markers in HTML. They come in pairs, like
  `<p>` (start) and `</p>` (end), with your words in between.
- **Placeholder** — a piece of TEMPORARY text meant to be replaced, written in
  CAPITALS in [square brackets] or ending in `_HERE` (like `CONTACT_EMAIL_HERE`).
- **PNG** — a common image file type. Your announcement picture is a PNG.

---

*Keep this guide handy. Ninety percent of "managing the website" is just Part 1:
swap the picture, edit four lines, click Commit.*
