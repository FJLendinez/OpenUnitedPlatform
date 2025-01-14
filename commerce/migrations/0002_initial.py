# Generated by Django 4.2.2 on 2023-08-11 08:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("commerce", "0001_initial"),
        ("product_management", "0001_initial"),
        ("talent", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="productaccountreservation",
            name="bounty_claim",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="talent.bountyclaim"
            ),
        ),
        migrations.AddField(
            model_name="productaccountdebit",
            name="bounty_claim",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="talent.bountyclaim"
            ),
        ),
        migrations.AddField(
            model_name="productaccountcredit",
            name="actioned_by",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="talent.person"
            ),
        ),
        migrations.AddField(
            model_name="productaccountcredit",
            name="organisation_account_debit",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                to="commerce.organisationaccountdebit",
            ),
        ),
        migrations.AddField(
            model_name="productaccountcredit",
            name="product_account",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                to="commerce.productaccount",
            ),
        ),
        migrations.AddField(
            model_name="productaccount",
            name="product",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                to="product_management.product",
            ),
        ),
        migrations.AddField(
            model_name="paymentorder",
            name="contributor_account",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                to="commerce.contributoraccount",
            ),
        ),
        migrations.AddField(
            model_name="outboundpayment",
            name="payment_order",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="commerce.paymentorder"
            ),
        ),
        migrations.AddField(
            model_name="organisationaccountdebit",
            name="organisation_account",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                to="commerce.organisationaccount",
            ),
        ),
        migrations.AddField(
            model_name="organisationaccountcredit",
            name="organisation_account",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                to="commerce.organisationaccount",
            ),
        ),
        migrations.AddField(
            model_name="organisationaccount",
            name="organisation",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="commerce.organisation"
            ),
        ),
        migrations.AddField(
            model_name="inboundpayment",
            name="sales_order",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="commerce.salesorder"
            ),
        ),
        migrations.AddField(
            model_name="grant",
            name="approving_bee_keeper",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="approver",
                to="talent.person",
            ),
        ),
        migrations.AddField(
            model_name="grant",
            name="nominating_bee_keeper",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="nominator",
                to="talent.person",
            ),
        ),
        migrations.AddField(
            model_name="grant",
            name="organisation_account",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                to="commerce.organisationaccount",
            ),
        ),
        migrations.AddField(
            model_name="grant",
            name="organisation_account_credit",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="commerce.organisationaccountcredit",
            ),
        ),
        migrations.AddField(
            model_name="contributorreward",
            name="contributor_account",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                to="commerce.contributoraccount",
            ),
        ),
        migrations.AddField(
            model_name="contributoraccountdebit",
            name="contributor_account",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                to="commerce.contributoraccount",
            ),
        ),
        migrations.AddField(
            model_name="contributoraccountdebit",
            name="payment_order",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="commerce.paymentorder"
            ),
        ),
        migrations.AddField(
            model_name="contributoraccountcredit",
            name="bounty_claim",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="talent.bountyclaim"
            ),
        ),
        migrations.AddField(
            model_name="contributoraccountcredit",
            name="contributor_account",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                to="commerce.contributoraccount",
            ),
        ),
        migrations.AddField(
            model_name="contributoraccountcredit",
            name="contributor_reward",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                to="commerce.contributorreward",
            ),
        ),
        migrations.AddField(
            model_name="contributoraccountcredit",
            name="payment_order",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="commerce.paymentorder"
            ),
        ),
        migrations.AddField(
            model_name="contributoraccount",
            name="owner",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="talent.person"
            ),
        ),
        migrations.AddField(
            model_name="cart",
            name="creator",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="talent.person"
            ),
        ),
        migrations.AddField(
            model_name="cart",
            name="organisation_account",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                to="commerce.organisationaccount",
            ),
        ),
    ]
