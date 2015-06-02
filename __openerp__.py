{
   'name': 'UK customised reports',
   'version': '0.1',
   'category': 'Reporting',
   'description': """
   Customised reports for UK:
    - Sales order / Quotation
    - Account balance / overdue
    - Invoice print 

    These have been migrated from V3.3, V4, V5, V6, V6.1 to V8

   """,
   'author': 'OpusVL',
   'website': 'http://opusvl.com',
   'depends': ['account_accountant', 'sale', 'report'],
   'init_xml': [],
   'update_xml': [
       'reports.xml',
   ],
   'demo_xml': [],
   'test': [],
   'installable': True,
   'active': False,
}
