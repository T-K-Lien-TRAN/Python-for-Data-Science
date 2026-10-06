from datetime import datetime, timezone
import time

seconds = time.time()
today = datetime.now()
epoch = datetime.fromtimestamp(0, timezone.utc)
print(f"Seconds since {epoch.strftime('%B %d, %Y')}:", f"{seconds:,.4f} or {seconds:.2e} in scientific notation")
print(today.strftime('%b %d %Y'))