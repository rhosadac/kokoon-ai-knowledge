Combined schema.org JSON-LD for Kokoon Hotel Banyuwangi
====================================================

Two files ready to inject into WordPress header:

1. Hotel + Review schema:  schema-inject.html  (7.7 KB)
2. FAQPage schema:         faq-schema-inject.html  (16 KB)

HOW TO INJECT (WordPress - no visual change):

=== METHOD A: Plugin (easiest, recommended) ===

1. Install plugin "Insert Headers and Footers" or "WPCode"
2. Copy contents of schema-inject.html
3. Paste in header/footer section
4. Do same for faq-schema-inject.html
5. Save → Done. Zero visual change.

=== METHOD B: Theme header.php ===

1. In WordPress admin: Appearance → Theme File Editor
2. Open header.php
3. Paste <script> contents BEFORE </head> tag
4. Save

=== METHOD C: Elementor Pro ===

1. Edit page with Elementor
2. Add "HTML" widget anywhere (hidden section)
3. Paste the <script> block
4. Set visibility: hidden via CSS or place at bottom

====================================================
QUICK REFERENCE - What each file does:

schema-inject.html
  - Tells Google/AI: This is a Hotel
  - Shows rating: 93.6/100 from 6,572 reviews
  - Lists all amenities (pool, spa, EV charging, rooftop, etc.)
  - Shows room types and prices
  - Lists nearby attractions with distances
  - Shows 4 real guest reviews

faq-schema-inject.html
  - Tells Google/AI: These are 50 real FAQs
  - Answers questions like "Which hotel is best before Ijen?"
  - This is what AI Overviews and ChatGPT pull from
  - Massive GEO boost

====================================================
BOTH FILES CAN BE PASTED INTO THE SAME <script> TAG:

<script type="application/ld+json">
{ ...Hotel schema... }
</script>
<script type="application/ld+json">
{ ...FAQ schema... }
</script>
