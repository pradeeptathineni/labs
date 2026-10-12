# Join Members, Bookings, and Facilities

Source: [PostgreSQL Exercises](https://pgexercises.com/questions/joins/threejoin.html)

## Problem

Join three relational tables and verify duplicate handling, projection, and result ordering.

Follow the linked exercise for its requirements. The checks below define what I want to verify in my attempt; extensions are my additions.

## Before starting

The free browser query runner is enough. A local PostgreSQL setup is optional; inspect dataset terms before retaining the sample database. Keep the source’s published answer hidden until after the attempt.

## Checks

- Save the personal query and compare its rows and ordering with the source’s expected results.
- Explain the intermediate join relationships and why repeated bookings can produce duplicate output.
- Extension: compare results before and after deduplication and explain the difference.
