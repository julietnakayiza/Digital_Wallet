# Generated by Django 4.1 on 2022-08-19 12:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('account_name', models.CharField(max_length=15, null=True)),
                ('account_number', models.IntegerField()),
                ('account_type', models.CharField(choices=[('W', 'Withdrawal'), ('S', 'Savings'), ('D', 'Deposits')], max_length=15)),
                ('balance', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=20, null=True)),
                ('last_name', models.CharField(max_length=20, null=True)),
                ('address', models.CharField(max_length=15)),
                ('email', models.EmailField(max_length=254)),
                ('phone_number', models.CharField(max_length=15, null=True)),
                ('gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female')], max_length=15, null=True)),
                ('age', models.PositiveBigIntegerField()),
                ('id_number', models.CharField(max_length=15, null=True)),
                ('nationality', models.CharField(max_length=15, null=True)),
                ('profile_picture', models.ImageField(null=True, upload_to='profile_picture/')),
            ],
        ),
        migrations.CreateModel(
            name='Wallet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('User_id', models.IntegerField()),
                ('balance', models.IntegerField()),
                ('Amount', models.IntegerField()),
                ('time', models.DateTimeField()),
                ('status', models.CharField(max_length=15, null=True)),
                ('history', models.DateTimeField()),
                ('pin', models.CharField(max_length=15, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('transaction_code', models.CharField(max_length=15, null=True)),
                ('transaction_amount', models.IntegerField()),
                ('transaction_number', models.IntegerField()),
                ('transaction_type', models.CharField(choices=[('D', 'Debit'), ('C', 'Credit')], max_length=15)),
                ('transaction_fee', models.IntegerField()),
                ('transaction_time', models.DateField()),
                ('destination_account', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='transaction_destination', to='Digitalwallet.account')),
                ('origin_account', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='transaction_origin', to='Digitalwallet.account')),
                ('wallet_one', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Transaction_wallet', to='Digitalwallet.wallet')),
            ],
        ),
        migrations.CreateModel(
            name='ThirdParty',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('party_name', models.CharField(max_length=15, null=True)),
                ('party_id', models.PositiveSmallIntegerField()),
                ('phone_number', models.IntegerField()),
                ('account', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ThirdParty_account', to='Digitalwallet.account')),
            ],
        ),
        migrations.CreateModel(
            name='Reward',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reward_date', models.DateTimeField()),
                ('gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female')], max_length=15)),
                ('reward_points', models.IntegerField()),
                ('transaction', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reward_transaction', to='Digitalwallet.transaction')),
            ],
        ),
        migrations.CreateModel(
            name='Receipt',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('receipt_type', models.CharField(max_length=8, null=True)),
                ('receipt_date', models.DateTimeField()),
                ('receipt_file', models.FileField(upload_to='')),
                ('total_amount', models.IntegerField()),
                ('account_number', models.IntegerField()),
                ('transaction', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='receipt_transaction', to='Digitalwallet.transaction')),
            ],
        ),
        migrations.CreateModel(
            name='Notifications',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('customer_name', models.CharField(max_length=15, null=True)),
                ('notification_date_time', models.DateTimeField()),
                ('notification_status', models.CharField(choices=[('R', 'Read'), ('U', 'Unread')], max_length=1)),
                ('recipient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='notification_recipient', to='Digitalwallet.receipt')),
            ],
        ),
        migrations.CreateModel(
            name='Loan',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('loan_number', models.IntegerField()),
                ('loan_type', models.CharField(max_length=15, null=True)),
                ('loan_amount', models.IntegerField()),
                ('loan_date', models.DateTimeField()),
                ('interest_rate', models.IntegerField()),
                ('loan_due_date', models.DateTimeField()),
                ('loan_balance', models.IntegerField()),
                ('loan_term', models.IntegerField()),
                ('loan_guaranter', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='loan_loan', to='Digitalwallet.customer')),
                ('wallet', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='loan_wallet', to='Digitalwallet.wallet')),
            ],
        ),
        migrations.CreateModel(
            name='Card',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('card_name', models.CharField(max_length=15, null=True)),
                ('card_number', models.IntegerField()),
                ('card_type', models.CharField(choices=[('C', 'Credit card'), ('D', 'Debit card')], max_length=15)),
                ('cvv_code', models.IntegerField()),
                ('card_issuer', models.CharField(choices=[('V', 'Visa'), ('M', 'Master card')], max_length=15)),
                ('date_issued', models.DateTimeField()),
                ('expiry_date', models.DateTimeField()),
                ('card_status', models.CharField(max_length=15, null=True)),
                ('account', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='card_account', to='Digitalwallet.account')),
                ('wallet', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='card_wallet', to='Digitalwallet.wallet')),
            ],
        ),
        migrations.AddField(
            model_name='account',
            name='wallet',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='account_wallet', to='Digitalwallet.wallet'),
        ),
    ]