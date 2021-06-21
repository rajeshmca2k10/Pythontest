import unittest
# from SEG.DB.DBConn import DBConn as db_util
# from bin import compliance_data_loader
# import bin.date_util as util
# import logging
import sys
import mock
import os
sys.path.append(os.path.dirname(__file__) + "/..")
from expert_networks.process_glg_data import __glg_login
# from selenium import webdriver

class TestDetermineRestrictedHistory(unittest.TestCase):

	def test_data(self):
		# print(dir(process_glg_data.__glg_login))
		a= TestDetermineRestrictedHistory()
		
		a.__glg_login("hfhf", "hjhj","args.sele_driver","args.sele_log_dir")

		

		# dd = process_glg_data.__glg_login(glg_url="hfhf", email_address ="hjhj", driver_location =" args.sele_driver", selenium_log_dir= "args.sele_log_dir")
		# print(dd)







if __name__ == "__main__":
    unittest.main()