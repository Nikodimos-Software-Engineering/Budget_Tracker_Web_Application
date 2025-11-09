from django.db import migrations


def create_categories(apps, schema_editor):
    Category = apps.get_model("finance", "Category")
    defaults = [
        # Income
        ("Salary", "income"),
        ("Bonus", "income"),
        ("Interest", "income"),
        ("Dividends", "income"),
        ("Investment Income", "income"),
        ("Gift", "income"),
        ("Refund", "income"),
        ("Other Income", "income"),
        # Expenses
        ("Rent / Mortgage", "expense"),
        ("Utilities", "expense"),
        ("Internet / Phone", "expense"),
        ("Groceries", "expense"),
        ("Eating Out", "expense"),
        ("Transportation", "expense"),
        ("Fuel", "expense"),
        ("Insurance", "expense"),
        ("Health / Medical", "expense"),
        ("Education", "expense"),
        ("Entertainment", "expense"),
        ("Subscriptions", "expense"),
        ("Shopping", "expense"),
        ("Clothing", "expense"),
        ("Personal Care", "expense"),
        ("Travel", "expense"),
        ("Taxes", "expense"),
        ("Fees & Charges", "expense"),
        ("Home Maintenance", "expense"),
        ("Childcare", "expense"),
        ("Pets", "expense"),
        ("Gifts & Donations", "expense"),
        ("Debt Payment", "expense"),
        ("Savings Transfer", "expense"),
        ("Miscellaneous", "expense"),
    ]

    for name, typ in defaults:
        Category.objects.get_or_create(name=name, type=typ)


def remove_categories(apps, schema_editor):
    Category = apps.get_model("finance", "Category")
    names = [
        "Salary",
        "Bonus",
        "Interest",
        "Dividends",
        "Investment Income",
        "Gift",
        "Refund",
        "Other Income",
        "Rent / Mortgage",
        "Utilities",
        "Internet / Phone",
        "Groceries",
        "Eating Out",
        "Transportation",
        "Fuel",
        "Insurance",
        "Health / Medical",
        "Education",
        "Entertainment",
        "Subscriptions",
        "Shopping",
        "Clothing",
        "Personal Care",
        "Travel",
        "Taxes",
        "Fees & Charges",
        "Home Maintenance",
        "Childcare",
        "Pets",
        "Gifts & Donations",
        "Debt Payment",
        "Savings Transfer",
        "Miscellaneous",
    ]
    Category.objects.filter(name__in=names).delete()


class Migration(migrations.Migration):

    dependencies = [("finance", "0001_initial")]

    operations = [
        migrations.RunPython(create_categories, remove_categories),
    ]
