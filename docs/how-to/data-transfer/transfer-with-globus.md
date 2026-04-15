# Transfer files with Globus

## When to use this

Use Globus when you need to:

- transfer large datasets (hundreds of GB to TB+)
- move data between systems (e.g. HPC, storage services)
- run reliable, unattended transfers
- ensure data integrity during transfer

If your transfer is small or primarily human-driven, consider Nextcloud instead.

---

## Before you start

Make sure you have:

- a UCT account
- access to the source data (e.g. local machine, HPC, or storage system)
- access to the destination system
- both systems available as Globus endpoints (or the ability to create one)

---

## Log in to Globus

1. Go to https://app.globus.org
2. Select your institution login.
3. Authenticate using your UCT credentials.

---

## Identify your endpoints

An endpoint is a system that can send or receive data.

Typical endpoints include:
- HPC systems
- institutional storage
- your local machine (via Globus Connect Personal)

### To use your local machine

1. Install Globus Connect Personal.
2. Set up a local endpoint.
3. Ensure it is running during transfers.

---

## Transfer data between endpoints

1. In the Globus web interface, open the **File Manager**.
2. Select your **source endpoint**.
3. Navigate to the source folder.
4. Select your **destination endpoint**.
5. Navigate to the destination folder.
6. Select the files or folders to transfer.
7. Click **Start**.

Globus will:
- queue the transfer
- retry automatically if needed
- verify file integrity

You do not need to keep your browser open once the transfer has started.

---

## Monitor transfer progress

1. Go to the **Activity** or **Transfers** section.
2. View status:
   - active
   - completed
   - failed

If a transfer fails, Globus will typically retry automatically.

---

## Good practice

- Transfer directories rather than many individual files where possible.
- Avoid modifying files while they are being transferred.
- Use clear folder structures before starting transfers.
- Confirm sufficient storage space at the destination.
- For HPC workflows, transfer data to the correct storage location (e.g. RDS or scratch as appropriate).

---

## When to use something else

Use another method if:

- the transfer is small and ad hoc → use Nextcloud
- the workflow is simple and local → use scp or rsync
- you need browser-based sharing with non-technical users → use Nextcloud

---

## Related pages

- `services/data-transfer/index.md`
- `how-to/data-transfer/transfer-with-nextcloud.md`
- `reference/storage/rds.md`