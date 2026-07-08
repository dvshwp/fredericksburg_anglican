# HTML for Beginners — A Guide Built Around *Your* Website

*Everything here is explained using the real code in this project, so you can open
`index.html`, find the exact tags below, and see them doing their job.*

---

## 1. What is HTML?

**HTML** stands for **HyperText Markup Language**. It's the language every web
page is written in. It is *not* a programming language with math and logic — it's
a **markup** language, which means you take plain text and wrap pieces of it in
labels that tell the browser what each piece *is*: "this is a heading," "this is a
paragraph," "this is an image."

A web browser (Chrome, Safari, Firefox) reads the HTML and draws the page.

---

## 2. The single most important idea: tags

A **tag** is a label written inside **angle brackets**: `< >`.

Most tags come in a **pair** — an opening tag and a closing tag. The closing tag
has a slash `/`. Whatever you put *between* them is the content:

```
<p>Welcome to our church.</p>
 ▲        ▲                ▲
 opening  your content     closing (note the slash)
 tag                       tag
```

- `<p>` says "a paragraph starts here."
- `</p>` says "the paragraph ends here."
- Together, the opening tag + content + closing tag make one **element**.

**Tag vs. element** (a question people love to ask): the *tags* are the `<p>` and
`</p>` marks; the whole thing — tags **and** the content inside — is the
**element**. In everyday talk people say "tag" for both, and that's fine.

### Tags that don't have a closing tag ("empty" tags)

A few tags don't wrap any content, so they have **no closing tag**. They're
called **empty** or **void** elements. In your site, `<img>` (an image) and
`<hr>` (a divider line) are like this — they stand alone:

```
<hr>
<img src="favicon.svg" alt="">
```

### Attributes: giving a tag extra information

Inside an opening tag you can add **attributes** — little `name="value"` settings
that give the tag extra instructions. For example, a link needs to know *where*
it goes, so it uses an `href` attribute:

```
<a href="events.html">Events</a>
   ▲    ▲
   │    the value (where the link points)
   the attribute name
```

Attributes always live **inside the opening tag**, and their values go in
`"double quotes"`. A tag can have several attributes separated by spaces.

### Nesting: tags inside tags

Tags can go **inside** other tags. When they do, you close them in the reverse
order you opened them — like closing a set of boxes, innermost first:

```
<p>Come to <strong>Sunday worship</strong> with us.</p>
```

Here a `<strong>` element sits *inside* a `<p>` element. Think of it like nesting
boxes: the inner box (`strong`) must close before the outer box (`p`).

### Comments: notes the browser ignores

Anything between `<!--` and `-->` is a **comment**. The browser skips it
completely. Your site is full of these — they're notes to help humans understand
the code:

```
<!-- This is a comment. It won't appear on the page. -->
```

### The very first line: `<!DOCTYPE html>`

Every page starts with `<!DOCTYPE html>`. It isn't really a tag — it's a signal
that says "this document is modern HTML." Just always put it at the top and move
on.

---

## 3. Read a real line together

Here's an actual line from your site. See if you can name every part:

```
<img class="event-image" src="images/next_event.png" alt="Announcement for our next gathering; details in the image.">
```

- `<img …>` — an **image** element (empty tag, no closing tag).
- `class="event-image"` — an **attribute** that labels this image so the
  stylesheet can style it.
- `src="images/next_event.png"` — the **source**: which image file to show.
- `alt="…"` — the **alt text**: a description read aloud to blind visitors and
  shown if the image fails to load.

Once you can read that line, you can read almost any line of HTML.

---

## 4. Tag Dictionary — tags used in THIS website

These are **every** tag that appears in `index.html` and `events.html`, grouped
by the job they do. Open the files and hunt for each one!

### Page skeleton (the structure every page needs)

**`<!DOCTYPE html>`** — The opening signal that says "modern HTML." One per page,
right at the top. Not a normal tag (no closing tag).

**`<html>`** — The container for the *entire* page; everything else lives inside
it. In your site it also carries `lang="en"` to say the page is in English:
`<html lang="en">`.

**`<head>`** — The "behind the scenes" section. Nothing here is shown on the page
itself; it holds the page's title, description, icons, and links to styling. Comes
before `<body>`.

**`<body>`** — Everything a visitor actually **sees** goes inside `<body>`:
headings, paragraphs, images, links — all of it.

### Inside the head (information *about* the page)

**`<title>`** — The page's name. It shows in the **browser tab** and as the big
blue link in Google results. Example: `<title>Fredericksburg Anglican
Fellowship | …</title>`.

**`<meta>`** — Gives the browser and search engines facts about the page, such as
the character set, the mobile-scaling setting, the search description, and the
social-share preview. It's an empty tag. Your site uses several, e.g.
`<meta name="description" content="…">`.

**`<link>`** — Connects this page to another file. Your site uses it to attach the
stylesheet (`<link rel="stylesheet" href="css/style.css">`) and the little tab
icons (favicons). Empty tag. *(Note: this is NOT a clickable link — that's `<a>`,
below.)*

**`<script>`** — Holds code or data for the browser. In your site it isn't
programming — it holds the **structured data** (a block of facts about the church
in a format Google reads). It has an opening and closing tag.

### Layout landmarks (big labelled regions of the page)

**`<header>`** — The top banner of the page: the church name and cross. (Don't
confuse this with `<head>`, which is invisible — `<header>` is visible.)

**`<nav>`** — A block of **navigation** links (your Home / Events menu). Labelling
it `<nav>` helps screen readers announce "navigation."

**`<main>`** — The main content of the page — the unique stuff, as opposed to the
header and footer that repeat on every page. There should be only one `<main>`.

**`<section>`** — A themed chunk of the page, like "Welcome," "Our next
gathering," or "Give." Sections group related content together.

**`<footer>`** — The bottom strip of the page: church name again, diocese link,
give and contact links.

### Everyday content tags

**`<h1>`** — The **number-one heading** — the single most important title on the
page. Your site uses it for the church name in the header. Use only **one `<h1>`**
per page.

**`<h2>`** — A **second-level heading**, used for each section's title ("You are
welcome here," "Our next gathering," etc.). Headings go in order of importance:
`<h1>` then `<h2>` then `<h3>`…

**`<p>`** — A **paragraph** of text. The most common tag on the whole site.

**`<a>`** — An **anchor**, better known as a **link**. The `href` attribute says
where it goes. It can point to another page (`href="events.html"`), a web address
(`href="https://…"`), or an email (`href="mailto:someone@example.com"`).

**`<strong>`** — Marks text as **important**, and browsers show it **bold**. Your
site uses it to emphasise phrases like "Anglican Church in North America."

**`<span>`** — An **invisible little wrapper** around a piece of text so it can be
styled differently, without starting a new line. Your site wraps the labels
("What:", "Date:") in `<span class="label">` so they can be coloured and bolded.

**`<div>`** — A plain **box/container** used to group things for layout or
styling. It has no meaning of its own — it's just scaffolding. Your site uses one
for the "next gathering" details card: `<div class="details-card">`.

### Lists

**`<ul>`** — An **unordered list** (a bullet-point list). It's the container.

**`<li>`** — A **list item** — one bullet. Each event under "On the calendar" is
an `<li>` inside the `<ul>`. Structure looks like:

```
<ul>
  <li>First thing</li>
  <li>Second thing</li>
</ul>
```

### Media & dividers

**`<img>`** — An **image**. Empty tag. Needs a `src` (which file) and should
always have `alt` (a text description) for accessibility. Your announcement
picture and the cross icons are `<img>` elements.

**`<hr>`** — A **horizontal rule**: a divider between sections. Empty tag. Your
site styles it as the thin gold line between sections.

---

## 5. Mini-dictionary of the attributes your site uses

Attributes are the `name="value"` settings inside a tag.

- **`lang`** — the language of the page. `<html lang="en">` = English.
- **`charset`** — the set of characters the page uses. `<meta charset="UTF-8">`
  lets you use any letter or symbol safely.
- **`name`** / **`content`** — used together on `<meta>` tags: `name` says *what
  kind* of info, `content` gives *the value* (e.g. the description text).
- **`property`** — like `name`, but used for the social-share (Open Graph) meta
  tags.
- **`rel`** — describes the *relationship* of a `<link>`, e.g.
  `rel="stylesheet"` (this link is our styling) or `rel="icon"` (this is a tab
  icon).
- **`href`** — the destination of a link (`<a>`) or a `<link>`. Short for
  "hypertext reference."
- **`src`** — the **source** file for an image or script (which file to load).
- **`alt`** — the text description of an image, for screen readers and for when an
  image can't load.
- **`type`** — what *kind* of thing something is, e.g.
  `type="image/png"` on an icon link.
- **`sizes`** — the pixel size of an icon, e.g. `sizes="64x64"`.
- **`class`** — a **label you invent** and attach to elements so the stylesheet
  (`style.css`) can style everything with that label the same way. You can reuse
  the same class on many elements.
- **`id`** — a **unique label** for **one** element (used once per page). Your
  "Our next gathering" section has `id="next"` so links can jump straight to it
  with `#next`.
- **`aria-label`** — a hidden label that helps screen readers describe something
  (used on your `<nav>` so it's announced as "Primary" navigation).

> **`class` vs `id` — the classic confusion:** a **class** can be used on *many*
> elements (like a category everyone can belong to); an **id** must be used on
> only *one* element (like a name tag for a single person).

---

## 6. Other common tags — NOT used in this website (yet)

> ⚠️ **None of the tags below appear in your current site.** They're here as a
> reference so you recognise them when you see them elsewhere, and so you know
> what's available if you ever want to add a feature.

### More headings
- **`<h3>`, `<h4>`, `<h5>`, `<h6>`** — smaller sub-headings. `<h3>` sits under an
  `<h2>`, and so on down to the tiny `<h6>`. (Your site only needed `<h1>` and
  `<h2>`.)

### More text formatting
- **`<em>`** — *emphasis*, shown in italics (the italic cousin of `<strong>`).
- **`<b>`** — bold text with no special importance (use `<strong>` for genuine
  importance instead).
- **`<i>`** — italic text with no special meaning.
- **`<br>`** — a single **line break** (an empty tag). Forces text to a new line.
- **`<small>`** — smaller print, like fine print.
- **`<blockquote>`** — a block of quoted text, usually indented.
- **`<code>`** — text shown in a monospace "computer" font, for code snippets.
- **`<pre>`** — "preformatted" text that keeps your exact spacing and line breaks.

### Ordered lists
- **`<ol>`** — an **ordered** (numbered) list. Same idea as `<ul>`, but items get
  numbers 1, 2, 3 instead of bullets. It still holds `<li>` items inside.

### Tables (rows and columns of data)
- **`<table>`** — the container for a table.
- **`<tr>`** — a table **row**.
- **`<th>`** — a **header cell** (bold, for column titles).
- **`<td>`** — a normal **data cell**.

### Forms (collecting input from visitors)
- **`<form>`** — a container for input fields.
- **`<input>`** — a single field: a text box, checkbox, etc. (empty tag).
- **`<label>`** — the caption that names an input.
- **`<textarea>`** — a large multi-line text box.
- **`<select>`** and **`<option>`** — a drop-down menu and its choices.
- **`<button>`** — a clickable button.

*(Forms usually need extra code on a server to actually receive the information,
which is why this site uses a simple email link instead.)*

### More page-structure landmarks
- **`<article>`** — a self-contained piece of content, like a single blog post or
  news item.
- **`<aside>`** — content off to the side, like a sidebar or a related note.
- **`<figure>`** and **`<figcaption>`** — an image (or diagram) together with a
  caption underneath it.
- **`<details>`** and **`<summary>`** — a click-to-expand "show more" box.

### Other media
- **`<video>`** — embeds a video player.
- **`<audio>`** — embeds an audio player.
- **`<iframe>`** — embeds another web page inside this one (for example, a Google
  Map or a YouTube video).

---

## 7. Try it yourself (safe practice)

You can experiment **without touching the real website**:

1. On your computer, make a new plain-text file and name it `practice.html`.
2. Paste this in and save:

   ```html
   <!DOCTYPE html>
   <html lang="en">
   <head>
     <title>My Practice Page</title>
   </head>
   <body>
     <h1>Hello!</h1>
     <p>This is <strong>my</strong> first web page.</p>
     <ul>
       <li>I can make lists</li>
       <li>I can make links: <a href="https://fredericksburganglican.org">our church</a></li>
     </ul>
   </body>
   </html>
   ```

3. **Double-click the file** to open it in your browser. You just built a web
   page!
4. Change the words, add another `<li>`, try an `<h2>`, and refresh the browser to
   see what happens. Break it, fix it — that's how everyone learns HTML.

---

## Quick reference: the tags in your site, at a glance

`<!DOCTYPE html>` · `<html>` · `<head>` · `<body>` · `<title>` · `<meta>` ·
`<link>` · `<script>` · `<header>` · `<nav>` · `<main>` · `<section>` ·
`<footer>` · `<h1>` · `<h2>` · `<p>` · `<a>` · `<strong>` · `<span>` · `<div>` ·
`<ul>` · `<li>` · `<img>` · `<hr>`

Learn these two dozen well and you'll understand the whole website — and most of
the web.
