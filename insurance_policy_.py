from odoo import models, fields

class InsurancePolicy(models.Model):
    _name = 'insurance.policy'
    _description = 'Insurance Policy Management'

    name = fields.Char('Policy Name', required=True)
    policy_type = fields.Selection([
        ('life', 'Life'),
        ('health', 'Health'),
        ('disability', 'Disability'),
    ], required=True, string="Policy Type")
    customer_id = fields.Many2one('res.partner', string='Customer')
    start_date = fields.Date('Start Date')
    end_date = fields.Date('End Date')
    premium_amount = fields.Float('Premium Amount')

