# Transfer files with Nextcloud

## When to use this

Use Nextcloud when you need to:

- receive files from external collaborators
- share files through a browser-based interface
- provide simple, secure access without requiring accounts or setup
- work with data stored in services such as RDS via a web interface

If your transfer is large, automated, or system-to-system, use :contentReference[oaicite:1]{index=1} instead.

---

## Before you start

Make sure you have:

- a UCT account
- access to Nextcloud
- a destination folder for incoming or shared files
- an appropriate storage location if the data is larger than the default allocation

If the data should be stored in RDS, ensure the RDS share is set up first.

---

## Log in to Nextcloud

1. Open the UCT Nextcloud site.
2. Sign in with your UCT credentials.
3. Open the Files view.

---

## Receive files using FileDrop

Use FileDrop when someone outside UCT needs to send you files.

1. Create or select a destination folder.
2. Open the sharing options for the folder.
3. Enable **FileDrop**.
4. Copy the generated upload link.
5. Send the link to the external collaborator.

The collaborator can:
- upload files

The collaborator cannot:
- view existing files
- browse the folder
- download files

---

## Share files with collaborators

1. Select the file or folder.
2. Open the sharing options.
3. Generate a share link or assign access.
4. Apply any restrictions if needed.
5. Send the link to the collaborator.

---

## Use Nextcloud with RDS

If your data is stored in RDS, you can use Nextcloud as a sharing layer.

Typical workflow:

1. Ensure the RDS share exists and you have access.
2. Connect the RDS share in Nextcloud (if available).
3. Navigate to the RDS-backed folder.
4. Share or receive files using FileDrop or links.

The data remains stored in RDS. Nextcloud provides the interface.

---

## Good practice

- Store research data in RDS or another appropriate storage service.
- Use Nextcloud for transfer and sharing, not primary storage.
- Use clearly named folders for incoming data.
- Review permissions before sharing.
- Move data out of temporary upload areas into structured storage.

---

## When to use something else

Use another method if:

- the dataset is large (hundreds of GB or more) → use Globus
- the transfer is system-to-system → use Globus
- the workflow is automated → use command-line tools
- the data must be directly available to HPC → use RDS

---

## Related pages

- `services/data-transfer/index.md`
- `how-to/data-transfer/transfer-with-globus.md`
- `reference/data-transfer/nextcloud.md`
- `reference/storage/rds.md`