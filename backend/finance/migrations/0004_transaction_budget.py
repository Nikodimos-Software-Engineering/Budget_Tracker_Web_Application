from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('finance', '0003_create_savingsgoal'),
    ]

    operations = [
        migrations.AddField(
            model_name='transaction',
            name='budget',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='transactions', to='finance.budget'),
        ),
    ]
