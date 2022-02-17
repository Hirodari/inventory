"""
    for crash test while coding
"""

from app.models.hardware import SSD

stg = SSD("HD", "fred", 10, 5, 25, "Interface 1")
print(repr(stg))
print(stg.capacity_gb)

