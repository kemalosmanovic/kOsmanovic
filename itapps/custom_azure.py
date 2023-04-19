from storages.backends.azure_storage import AzureStorage
import os
class AzureMediaStorage(AzureStorage):
    account_name = 'demostoragedjango' # Must be replaced by your <storage_account_name>
    account_key = os.environ['storagekey'] # Must be replaced by your <storage_account_key>
    azure_container = 'media'
    expiration_secs = None

class AzureStaticStorage(AzureStorage):
    account_name = 'demostoragedjango' # Must be replaced by your storage_account_name
    account_key = os.environ['storagekey'] # Must be replaced by your <storage_account_key>
    azure_container = 'static'
    expiration_secs = None