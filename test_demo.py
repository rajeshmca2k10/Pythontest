import unittest


class TestDetermineRestrictedHistory(unittest.TestCase):

	def test_data(self):
		# print(dir(process_glg_data.__glg_login))
		a= TestDetermineRestrictedHistory()
		
		a.__glg_login("hfhf", "hjhj","args.sele_driver","args.sele_log_dir")

		

		# dd = process_glg_data.__glg_login(glg_url="hfhf", email_address ="hjhj", driver_location =" args.sele_driver", selenium_log_dir= "args.sele_log_dir")
		# print(dd)







if __name__ == "__main__":
    unittest.main()
