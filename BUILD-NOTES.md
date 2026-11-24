# Build notes

This repo holds one small Python program, main.py, that writes a single
one-line joke about cats to the entry file. Nothing else is part of the
entry. The joke was written fresh for this bounty, in my own words, and
checked against the judge brief in the kit.

The joke is: my cat has never paid rent, never done a dish, and still
takes the sunny spot on the bed, so now I just call him my landlord.

Why this joke fits the brief: the setup lists three things the cat takes
without giving anything back, and the turn reframes the cat as the
landlord, which is a fresh angle rather than a familiar cat pun. It has
no purr wordplay and no litter-box joke. It is short, it needs no
explanation, and it is the kind of line a person could retell to a
friend the same day.

The program keeps the joke as one string constant, checks that it is
between 1 and 200 characters after trimming, creates the output folder
if needed, and writes exactly that line to the entry file, with no
trailing newline and no extra text.

Verification done locally: I ran the program and read back the entry
file, confirming it holds exactly the joke line and that the character
count is inside the 1 to 200 range. I also computed the file hash both
with and without a trailing newline so the parent can match whichever
form the grader reports.

Nothing here was submitted. The parent handles the GitHub repository,
the transcript bundle, and the submission. The badge links in the
readme assume the repository will be named the-one-line-cat-joke-that-lands
under donatfarm01; if the parent creates it under a different name,
the badge image paths in the readme need to be updated to match.
