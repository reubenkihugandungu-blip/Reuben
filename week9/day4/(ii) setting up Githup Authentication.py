# GitHub no longer accepts password authentication for git operations.
#  You use a Personal Access Token (PAT) or SSH keys. 
# SSH is more convenient for daily work because you authenticate once per machine.

# Step 1: Generate an SSH key pair
ssh-keygen -t ed25519 -C "brian@example.com"

# Press Enter to accept default file location
# Press Enter twice for no passphrase (or set one for extra security)

# Step 2: Copy the public key to clipboard
# Mac:
cat ~/.ssh/id_ed25519.pub | pbcopy
# Windows (Git Bash):
cat ~/.ssh/id_ed25519.pub | clip
# Linux:
cat ~/.ssh/id_ed25519.pub
# (then manually copy the output)

# Step 3: Go to github.com
# Settings > SSH and GPG keys > New SSH key
# Paste your public key and save

# Step 4: Test the connection
ssh -T git@github.com
Hi brianotieno! You've successfully authenticated, but GitHub does not provide shell access.

# Tip: Your public key (id_ed25519.pub) is safe to share. It is designed to be public. 
# Your private key (id_ed25519) never leaves your machine. Never paste, upload, or share the private key file.
