
# flake8: noqa

# Import all APIs into this package.
# If you have many APIs here with many many models used in each API this may
# raise a `RecursionError`.
# In order to avoid this, import only the API that you directly need like:
#
#   from .api.accounts_api import AccountsApi
#
# or import this package, but before doing it, use:
#
#   import sys
#   sys.setrecursionlimit(n)

# Import APIs into API package:
from ynab_api.api.accounts_api import AccountsApi
from ynab_api.api.budgets_api import BudgetsApi
from ynab_api.api.categories_api import CategoriesApi
from ynab_api.api.deprecated_api import DeprecatedApi
from ynab_api.api.months_api import MonthsApi
from ynab_api.api.payee_locations_api import PayeeLocationsApi
from ynab_api.api.payees_api import PayeesApi
from ynab_api.api.scheduled_transactions_api import ScheduledTransactionsApi
from ynab_api.api.transactions_api import TransactionsApi
from ynab_api.api.user_api import UserApi
