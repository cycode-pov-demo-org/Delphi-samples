"""
PoV test configuration.

This file is intentionally checked in to exercise Cycode's custom
secret-detection policy "Internal API Key (corp-prod)".

The value below is a fabricated test string that matches the policy regex
\\bcorp-prod-[a-f0-9]{20}\\b. It is NOT a real credential and corresponds
to no real system.
"""

INTERNAL_API_KEY = "corp-prod-0000000000aaaaaaaaaa"
