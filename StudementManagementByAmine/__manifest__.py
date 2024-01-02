{
    'name': 'My Student Management',
    'summary': "Student Management System",
    'sequence': 10,
    'description': "Student Management System By Amine",
    'author': "ABKADRI AMINE",
    'website': "https://odoo.com/app/Student_Management",
    'category': 'Students',
    'version': '1.0',
    'depends': ['base'],
    'data': [
        'views/student.xml',
        'views/department_views.xml'

    ],
    'demo': [],
    'installable': True,
    'application': True,
    'auto_install': True,
}