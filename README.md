# Ekonex Apps

Minimal Home Assistant catalog. Application source and container packages are not public here.
The installer must configure authorized read-only access to ghcr.io before installation.
Only amd64 is currently validated for the included releases.

Existing installations on other catalogs are not migrated by adding this repository.
Migration requires a verified backup and the dedicated installer procedure to preserve data.
Initial boot is manual to prevent two hardware gateways starting together during migration.
The installer restores the intended boot policy after successful verification.
Automatic updates are not enabled by this catalog.

Distribution versions dist1/dist2 identify packaging revisions, not additional app features.
