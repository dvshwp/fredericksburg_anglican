# [CHURCH NAME] — Website

A small, fast, mobile-friendly website for an Anglican (ACNA) church plant in
Fredericksburg, Virginia — part of the **Diocese of the Mid-Atlantic**.

It is built with **plain HTML and CSS only** — no JavaScript, no frameworks, no
build step. That means it runs perfectly on **free GitHub Pages** hosting, and
it is simple enough for a beginner to read and change. Every file is heavily
commented to help someone learning web design.

---

## 1. What's in this folder (file structure)

```
church-website/
├── index.html            ← the HOME page (welcome, event image, info, give)
├── events.html           ← an OPTIONAL second page listing events
├── css/
│   └── style.css         ← ALL the colors, fonts, and layout live here
├── images/
│   └── next_event.png    ← the announcement image you overwrite to post events
├── favicon.svg           ← Jerusalem Cross tab icon (sharp, scalable version)
├── favicon.png           ← Jerusalem Cross tab icon (backup image version)
├── apple-touch-icon.png  ← icon used when someone saves the site to an iPhone
├── robots.txt            ← tells search engines they may index the site
├── sitemap.xml           ← a list of the pages, for search engines
├── CNAME                 ← holds your custom domain (for GitHub Pages)
├── build_images.py       ← optional helper that made the placeholder images
├── _guides/              ← how-to + HTML teaching guides (NOT part of the live site)
│   ├── MANAGING_THE_WEBSITE.md   ← plain-English guide for whoever updates the site
│   └── HTML_FOR_BEGINNERS.md     ← HTML lesson + dictionary of the site's tags
└── README.md             ← this file
```

You can ignore `build_images.py` entirely — it is only kept so you can see how
the placeholder graphics were generated. The website does not need it to run.

**About the `_guides/` folder:** it holds two reference documents (a plain-English
management guide and a beginner HTML lesson). They live in the repository so they
travel with the project and render nicely on github.com, **but they are not part
of the published website.** GitHub Pages ignores any folder whose name begins with
an underscore (`_`), so these files are never served at your web address and no
visitor will see them. (This is why you should *not* add a file named `.nojekyll` —
that would turn off this behavior and make the folder web-accessible.)

---

## 2. ⭐ How to update the upcoming event (the important one)

Updating an event is **two quick steps** — swap one image, then edit four lines
of text. It stays simple, but now your event details are also readable by Google
and AI assistants (see "Why two steps?" below).

**Step 1 — Replace the announcement image.**
1. Make your new announcement graphic. Keep it a **tall portrait**, roughly a
   **5:7 shape** (the sample is 1061 × 1483 pixels). Bake the date, time,
   location, and details right into the picture.
2. Name the file **exactly** `next_event.png`.
3. Put it in the **`images/`** folder, replacing the old one (same name).

**Step 2 — Update the "Our next gathering" text.**
Open `index.html` and find the big star-marked comment:
`⭐ OUR NEXT GATHERING - UPDATE THIS WHENEVER YOU POST A NEW EVENT ⭐`.
Just below it is a card with four lines between arrow comments
(`↓↓↓ EDIT THESE FOUR LINES ↓↓↓`). Change the text after each colon to match
your new image:

```
What:     Sunday Worship & Holy Communion
Date:     Sunday, September 14, 2025
Time:     10:00 AM
Location: Grace Hall, 123 Main St, Fredericksburg, VA 22401
```

Only type between the `>` and `<` marks — don't touch the tags themselves.

**Then** save/commit and push to GitHub (see the GitHub Pages steps below). Both
the picture and the text update the moment you push. You only edit this text on
**one page** (`index.html`); the events page links to it, so there's nothing to
update twice.

**Keep the image small** so the page loads fast on phones — aim for a few hundred
KB or less. Always keep replacement images at roughly the same **5:7 portrait
proportions** and the exact filename **`images/next_event.png`**.

### Why two steps? (and why not a `next_event.txt` file?)

Great question — and the short answer is that a separate text file wouldn't
actually solve the problem it's meant to solve.

The date, time, and place inside `next_event.png` are just coloured pixels.
Google and AI assistants (ChatGPT, Perplexity, Claude, etc.) **cannot read text
that lives inside an image.** So if you only ever update the image, your event is
invisible to search and to AI — which is exactly the visibility you're trying to
win.

A `next_event.txt` file *sounds* tidy, but for it to appear on the page something
has to load it in. On a plain static site with no build step, the only way to do
that is a bit of **JavaScript** that fetches the file and injects it after the
page loads. The catch: **most AI crawlers (and, less reliably, Google) don't run
that JavaScript.** They read the raw HTML that arrives first — so text injected
by a script is often invisible to them. You'd add complexity and *still* not be
machine-readable. That defeats the whole purpose.

Editing the text directly in `index.html` puts the words in the raw HTML, where
every search engine and AI assistant can read them — guaranteed. And it's barely
more work than editing a `.txt` file: it's four labelled lines in one clearly
marked spot. That's why the recommended workflow is "swap the image **and** edit
those four lines," rather than a separate text file.

> Tip: once your gatherings settle into a regular weekly time, this gets even
> easier — you can write the standing day/time once and rarely touch it. See §7
> for the optional structured-data upgrade that can make a specific event
> eligible for Google's event listings.

---

## 3. Fill in your details (placeholders)

Open `index.html` and `events.html` in any text editor and use **Find & Replace**
to swap these placeholders for your real information. They appear in CAPITALS or
end in `_HERE` so they are easy to spot.

Your **domain** (`fredericksburganglican.org`) and **giving link**
(`https://secure.qgiv.com/for/dioceseofthemid-atlantic/`) are already filled in. These remain:

| Placeholder | Replace with | Found in |
|---|---|---|
| `[CHURCH NAME]` | Your church's name | index.html, events.html, README |
| `[WHAT ...]` / `[DATE ...]` / `[TIME ...]` | Your next event (see §2) | index.html |
| `[VENUE NAME]` / `[STREET ADDRESS]` | Where you meet | index.html |
| `[MEETING STREET ADDRESS]` / `[ZIP CODE]` | Address in the JSON-LD block | index.html |
| `CONTACT_EMAIL_HERE` | Your contact email | index.html, events.html |
| `SOCIAL_MEDIA_URL_HERE` | Facebook/Instagram link (optional) | index.html |

Tip: fill in your real **address and ZIP** in the `Church` structured-data block
near the top of `index.html` too — it helps you show up in local "church near me"
searches and in AI answers.

---

## 4. Put it online with GitHub Pages (free)

1. Create a free account at [github.com](https://github.com).
2. Make a new repository. For a personal site you can name it
   `YOURUSERNAME.github.io`, or use any name (e.g. `church-website`).
3. Upload **all the files in this folder** (keep the `css/` and `images/`
   folders intact). You can drag-and-drop them on GitHub's "Add file → Upload
   files" screen, or use Git if you know it.
4. In the repository, go to **Settings → Pages**.
5. Under "Build and deployment", set **Source** to *Deploy from a branch*, pick
   the **main** branch and the **/ (root)** folder, and click **Save**.
6. Wait a minute, then refresh. GitHub shows the live web address at the top of
   that Pages screen (something like `https://YOURUSERNAME.github.io/`).

To make changes later, edit the files and upload/commit them again — the live
site updates within a minute or two.

---

## 5. Connect a custom domain (optional)

> ⚠️ **If you are NOT using a custom domain yet, do not upload the `CNAME` file**
> (or delete it from the repo). While it still contains the placeholder
> `YOUR-DOMAIN-HERE.org`, GitHub Pages will try to use that fake domain and your
> normal `https://YOURUSERNAME.github.io/` address may stop loading. Add the
> `CNAME` file only once you have a real domain and have filled it in below.

If you own a domain (e.g. from Namecheap, Google Domains, etc.):

1. Open the **`CNAME`** file and replace `YOUR-DOMAIN-HERE.org` with your real
   domain — **just the bare domain, nothing else** (no `https://`, no comments).
   Example contents: `stmarysfredericksburg.org`
2. At your domain registrar, point the domain to GitHub Pages by adding the DNS
   records GitHub lists in **Settings → Pages → Custom domain**. (For an apex
   domain like `example.org` these are usually four `A` records; for a
   `www.` subdomain it's a `CNAME` record to `YOURUSERNAME.github.io`.)
3. Back in **Settings → Pages**, enter your domain in the **Custom domain**
   box and save, then tick **Enforce HTTPS** once it becomes available.
4. Finally, replace `YOUR-DOMAIN-HERE.org` with your real domain in:
   `index.html`, `events.html`, `robots.txt`, and `sitemap.xml` (search each
   file for that placeholder). This keeps your SEO links correct.

---

## 6. Colors and fonts used

Everything visual is controlled at the top of **`css/style.css`** in the
`:root { ... }` block. Change a value there and it updates across the whole site.

**Colors** (liturgical red + antique gold on a warm cream, matching the
announcement image):

| Name | Hex | Used for |
|---|---|---|
| Oxblood (deep burgundy) | `#6E1423` | header, footer, headings |
| Deep red | `#8A1C2B` | links, the Give button |
| Antique gold | `#B68A3E` | dividers, borders, the cross |
| Light gold / tan | `#D8BE8C` | soft highlights, footer text |
| Cream / ivory | `#FAF5EA` | page background |
| Charcoal | `#2A2521` | body text (strong contrast for readability) |

**Fonts** (two total, both already on nearly every device, so nothing to
download and the page stays fast):

- **Headings:** Georgia (a classic serif) — dignified and traditional.
- **Body text:** the system sans-serif (San Francisco on Apple, Segoe UI on
  Windows, Roboto on Android) — clean and highly readable.

Want fancier web fonts later (e.g. *EB Garamond* for headings)? Add one
`<link>` to Google Fonts in each page's `<head>`, then change `--font-heading`
in `style.css`. Not required, and it slightly slows loading, so system fonts are
the recommended default.

---

## 7. A couple of good-to-know notes

- **Google Business Profile:** For local "church near me" searches, a free
  [Google Business Profile](https://www.google.com/business/) matters as much as
  this website. Create one, verify your location, and add photos and service
  times. (There's a reminder comment in `index.html` too.)

- **Accessibility & mobile:** The site uses semantic HTML, alt text on images,
  strong color contrast, and a mobile-first responsive layout, so it works well
  on phones and with screen readers.

- **Your event details are already machine-readable.** The "Our next gathering"
  text block on the home page (§2) is real HTML text, so Google and AI assistants
  can read your next event's date, time, and location. Keeping it current is the
  second half of every event update.

- **Optional upgrade — make a specific event eligible for Google's event
  listings.** For most updates the text block above is enough. But if you want a
  particular event to be eligible for Google's rich *event* results, you can
  *optionally* add an `Event` structured-data block. Paste this just below the
  existing `Church` JSON-LD block in `index.html`, fill in the values, and push.
  Use the `startDate` format shown (year-month-day, then `T`, then 24-hour time).
  Delete or update it once the event has passed. **This is optional — skipping it
  breaks nothing.**

  ```html
  <script type="application/ld+json">
  {
    "@context": "https://schema.org",
    "@type": "Event",
    "name": "Sunday Worship & Holy Communion",
    "startDate": "2025-09-14T10:00",
    "eventAttendanceMode": "https://schema.org/OfflineEventAttendanceMode",
    "eventStatus": "https://schema.org/EventScheduled",
    "location": {
      "@type": "Place",
      "name": "VENUE NAME",
      "address": {
        "@type": "PostalAddress",
        "streetAddress": "123 Main St",
        "addressLocality": "Fredericksburg",
        "addressRegion": "VA",
        "postalCode": "22401",
        "addressCountry": "US"
      }
    },
    "organizer": {
      "@type": "Church",
      "name": "[CHURCH NAME]",
      "url": "https://fredericksburganglican.org/"
    },
    "image": "https://fredericksburganglican.org/images/next_event.png",
    "description": "Our next gathering. All are welcome."
  }
  </script>
  ```

- **When your schedule becomes regular:** you can add an
  `openingHoursSpecification` to the `Church` block for your standing weekly time.
  Ask for that snippet, or copy the Schema.org example — it's a small addition.

---

*Built as a clean, beginner-friendly teaching project. Keep it simple — the whole
point is that it's easy to read, easy to change, and easy to keep online.*
