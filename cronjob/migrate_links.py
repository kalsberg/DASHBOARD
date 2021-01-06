# Direct Imports
import xlrd
import os
import sys
import django
import getpass

# Relative Imports
from datetime import datetime

# Django Setup
STKDIR = os.path.abspath(r"..\..")
if STKDIR not in sys.path:
    sys.path.append(STKDIR)
from DASHBOARD import settings as project_settings

os.environ["DJANGO_SETTINGS_MODULE"] = "DASHBOARD.settings"
django.setup()
BASE_DIR = project_settings.BASE_DIR

# Project Imports
from django.contrib.auth.models import User
from links.models import HeaderLink, Category, SubCategory, Link, ContactInformation, FooterLink


def read_excel(file_path, sheet_name, columns, header_row=0, restrictions=None, end_row=None):
    """
    Retrieves data from a EXCEL file
    :param file_path: Path of the input file
    :param sheet_name: Excel sheet name
    :param columns: Column Names
    :param header_row: Header row number
    :param restrictions: Row value restrictions
    :param end_row: Last row number
    :return: data (dict)
    :author: Kalyani Soni (uidp2771) 16/03/2018
    :modified: Kalyani Soni (uidp2771) 16/03/2018
    """
    workbook = xlrd.open_workbook(file_path)
    worksheet = workbook.sheet_by_name(sheet_name)

    data = []
    keys = [v.value for v in worksheet.row(header_row)]
    end_row = worksheet.nrows if not end_row else end_row
    for row_number in range(end_row):
        if row_number <= header_row:
            continue
        row_data = {}
        for col_number, cell in enumerate(worksheet.row(row_number)):
            if keys[col_number] in columns:
                cell_type = cell.ctype
                if cell_type == 3:
                    cell_value = xlrd.xldate.xldate_as_datetime(cell.value, workbook.datemode
                                                                ).strftime('%d-%b-%Y')
                else:
                    cell_value = cell.value
                row_data[keys[col_number]] = cell_value
        if not restrictions:
            data.append(row_data)
        else:
            is_valid = True
            for restriction_key, restriction_values in restrictions.items():
                if row_data[restriction_key].strip().upper() not in [restriction_value.strip().upper()
                                                                     for restriction_value in restriction_values]:
                    is_valid = False
            if is_valid:
                data.append(row_data)

    return data


if __name__ == '__main__':
    # Logged User
    username = getpass.getuser()
    mdl_user, user_created = User.objects.get_or_create(username=username,
                                                        defaults={'last_login': datetime.now(), 'is_superuser': True})

    # Initialize
    path = r'D:\Projects\supporting_files\dashboard\data.xlsx'

    # Header Links
    HeaderLink.objects.all().delete()
    header_links_data = read_excel(path, 'Header', ('Name', 'Link'))
    for header_links_datum in header_links_data:
        HeaderLink.objects.create(name=header_links_datum['Name'], link=header_links_datum['Link'])

    # Content Links
    SubCategory.objects.all().delete()
    Link.objects.all().delete()
    content_links_data = read_excel(path, 'Links', ('Category', 'Sub Category', 'Link Name', 'Link Address'))
    for content_link_datum in content_links_data:
        print content_link_datum['Sub Category'], content_link_datum['Category']
        mdl_category, category_created = Category.objects.get_or_create(name=content_link_datum['Category'])
        mdl_sub_category, sub_category_created = SubCategory.objects.get_or_create(
            name=content_link_datum['Sub Category'], category=mdl_category)
        Link.objects.create(sub_category=mdl_sub_category, name=content_link_datum['Link Name'],
                            link=content_link_datum['Link Address'], added_by=mdl_user)

    # Contact Information
    ContactInformation.objects.all().delete()
    contact_info_data = read_excel(path, 'Contact', ('Escalation Level', 'Personell', 'Phone Number', 'Email'))
    for contact_info_datum in contact_info_data:
        ContactInformation.objects.create(escalation_level=contact_info_datum['Escalation Level'],
                                          personell=contact_info_datum['Personell'],
                                          phone_number=contact_info_datum['Phone Number'],
                                          email=contact_info_datum['Email'])

    # Footer Links
    FooterLink.objects.all().delete()
    footer_links_data = read_excel(path, 'Footer', ('Name', 'Link'))
    for footer_links_datum in footer_links_data:
        FooterLink.objects.create(name=footer_links_datum['Name'], link=footer_links_datum['Link'])