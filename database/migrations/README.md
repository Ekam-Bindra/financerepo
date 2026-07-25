# Database migrations

Application migrations will live in this directory once a database migration
tool is selected. The foundation intentionally does not create financial-domain
tables before their requirements and ownership are approved.

Migration requirements:

- changes must be forward-only and reviewed;
- every migration needs an explicit rollback or recovery procedure;
- tenant and authorization implications must be documented;
- financial data migrations must preserve lineage and audit relationships;
- CI must apply migrations against a clean PostgreSQL database.

