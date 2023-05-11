import re
from datetime import datetime
import json
from configuration.config_settings import ConfigSettingsClass
import os
import time


class OtherUtlClass:

    def get_current_date(self):
        now = datetime.now()
        # ddmmYY
        date_value = now.strftime("%d%m%Y")
        return date_value

    def get_current_time(self):
        now = datetime.now()
        # ddmmYY_HourMinSec
        date_time_value = now.strftime("%d%m%Y_%H%M%S")
        return date_time_value

    def create_new_screenshot_path_file(self, parent_dir, screenshot_name):
        file_name = screenshot_name + "_" + time.strftime("%d%m%y_%H%M%S")
        print(f"parent_dir: {parent_dir}")
        print(f"file name: {file_name}")
        path = os.path.join(parent_dir, file_name)
        return path


    def create_new_screenshot_folder(self, parent_dir, new_screenshot_dir):
        print(f" parent_dir: {parent_dir}, new_screenshot_dir: {new_screenshot_dir} ")
        path = os.path.join(parent_dir, new_screenshot_dir)
        try:
            os.mkdir(path)
            print(path)
            return True
        except OSError:
            error_msg = "new screenshot - failed to create directory, as it already exist"
            print(error_msg)
            return False

    def create_new_report_folder(self, parent_dir, new_report_dir):
        path = os.path.join(parent_dir, new_report_dir)
        try:
            os.mkdir(path)
            return path
        except OSError:
            error_msg = "create new report - failed to create directory"
            print(error_msg)
            return False

    def update_allure_report_path(self, generate_report_file_path, new_allure_report_path):
        print("report_dir_path " + generate_report_file_path)
        print("new_allure_report_path " + new_allure_report_path)
        # open file in read mode
        file = open(generate_report_file_path, "r")
        replaced_content = ""
        # looping through the file
        for line in file:
            # stripping line break
            line = line.strip()
            split_line = line.split(' ')
            current_allure_report_path_string = line.split(' ')[-1]
            # print("split_index_six: " + current_allure_report_path_string)
            # print("split_line: " + line)
            # print(new_allure_report_path)
            # stripping line break
            line = line.strip()
            # print(line)
            # replacing the texts
            new_line = line.replace(current_allure_report_path_string, new_allure_report_path)
            # print("new_line: " + new_line)
            # concatenate the new string and add an end-line break
            replaced_content = replaced_content + new_line + "\n"
            print("replaced_content:  " + replaced_content)

        # close the file
        file.close()
        # Open file in write mode
        write_file = open(generate_report_file_path, "w")
        # overwriting the old file contents with the new/replaced content
        write_file.write(replaced_content)
        # close the file
        write_file.close()

    def update_script_pytest_path(self, script_path):
        pytest_path = ConfigSettingsClass.pytest_path
        print(f"script_path: {script_path}")
        # open file in read mode
        file = open(str(script_path), "r")
        replaced_content = ""
        # looping through the file
        for line in file:

            # stripping line break
            line = line.strip()
            split_line = line.split(' ')
            current_pytest_path_string = line.split(' ')[0]
            pytest_is_same = current_pytest_path_string == pytest_path
            print(f"\nIs pytest path the same: {pytest_is_same}")

            if pytest_is_same is False:
                print("split_index_six: " + current_pytest_path_string)
                print("split_line: " + line)
                print("pytest_path: " + pytest_path)

                # stripping line break
                line = line.strip()
                # replacing the texts
                new_line = line.replace(current_pytest_path_string, pytest_path)
                print("new_line:  " + new_line)
                # concatenate the new string and add an end-line break
                replaced_content = replaced_content + new_line + "\n"
                print("replaced_content:  " + replaced_content)

                # close the file
                # file.close()
                # Open file in write mode
                write_file = open(str(script_path), "w")
                # overwriting the old file contents with the new/replaced content
                write_file.write(replaced_content)
                # close the file
                write_file.close()

        # close the file
        file.close()

    def check_report_dir_path_format(self, report_dir_path):
        # report_dir_path = "C:\\Users\\3app-hkdl-rpa-r01-st\\Documents\\HKDL_Automation\\dsp-web\\reports"

        if '/' in report_dir_path:
            print("report_dir_path has the forward slash")
            return 'forward_slash'
        elif '\\' in report_dir_path:
            print("report_dir_path has the back slash")
            return 'back_slash'

    def update_bat_file_alluredir_option(self, report_dir_path):

        # print(f"report_dir_path {report_dir_path}")
        script_path_file = f"{ConfigSettingsClass.execution_script_path}{ConfigSettingsClass.executable_file_name}"
        # print("script_path {script_path_file}")

        dir_format_seperator = self.check_report_dir_path_format(report_dir_path)
        print(f"dir_format_seperator: {dir_format_seperator}")

        new_alluredir_path = ""
        if dir_format_seperator == 'forward_slash':
            new_alluredir_path = f"--alluredir={report_dir_path}/"
            print(f"new_alluredir_path: {new_alluredir_path}")
        elif dir_format_seperator == 'back_slash':
            new_alluredir_path = f"--alluredir={report_dir_path}\\"
            print(f"new_alluredir_path: {new_alluredir_path}")

        # open file in read mode
        file = open(script_path_file, "r")
        replaced_content = ""
        # looping through the file
        for line in file:
            # stripping line break
            line = line.strip()

            split_line = line.split(' ')
            current_alluredir_string = line.split(' ')[-1]

            # print(f"split_index_six: {current_alluredir_string}")
            # print(f"split_line: {line}")
            # print(new_alluredir_path)
            # stripping line break
            line = line.strip()
            # replacing the texts
            new_line = line.replace(current_alluredir_string, new_alluredir_path)
            # print(f"new_line: {new_line}")
            # concatenate the new string and add an end-line break
            replaced_content = replaced_content + new_line + "\n"
            print(f"replaced_content: {replaced_content}")

        # close the file
        file.close()
        # Open file in write mode
        write_file = open(script_path_file, "w")
        # overwriting the old file contents with the new/replaced content
        write_file.write(replaced_content)
        # close the file
        write_file.close()
        return new_alluredir_path

    def get_screenshot_dir_file(self):
        # file_name = screenshot_name + "_" + time.strftime("%d%m%y_%H%M%S")
        #print(f"file_name is: {file_name}")
        ss_dir = self.create_new_screenshot_folder(ConfigSettingsClass.screenshot_path, self.get_current_date())
        print(f"inside get_screenshot_dir_file ss_dir variable is, {ss_dir}")
        # screenshot_file_name = file_name
        #print(f"inside get_screenshot_dir_file screenshot_path variable is, {screenshot_file_name}")
        # screenshot_path = ss_dir + "/" + file_name
        return ss_dir

    def take_screenshot(self, path_file, browser):
        try:
            screenshot = browser.save_screenshot(f"{path_file}.png")
            return f"Screenshot save successfully to directory file : {path_file}"
        except():
            return "Unable to take screenshot"

    def get_hkdl_folder_path(self):
        config_path = ConfigSettingsClass.config_path
        with open(config_path) as config_file:
            config = json.load(config_file)
        # Validate url and return url choice
        if 'hkdl_path' not in config:
            # exception is raised if config file doesn't contain url path
            raise Exception('The config file does not contain "hkdl_path"')
        hkdl_folder_path = config['hkdl_path']
        return hkdl_folder_path

    def get_current_config_url(self):
        config_path = ConfigSettingsClass.config_path
        with open(config_path) as config_file:
            config = json.load(config_file)
        # Validate url and return url choice
        if 'url_select' not in config:
            # exception is raised if config file doesn't contain url path
            raise Exception('The config file does not contain "url_select"')
        config_url_run = config['url_select']
        return config_url_run

    def check_config_url_is_prod(self):
        config_path = ConfigSettingsClass.config_path
        with open(config_path) as config_file:
            config = json.load(config_file)
        # Validate url and return url choice
        if 'url_select' not in config:
            # exception is raised if config file doesn't contain url path
            raise Exception('The config file does not contain "url_select"')
        config_url_run = config['url_select']
        if config_url_run == 'prod':
            val = True
            return bool(val)
        elif config_url_run == 'stage':
            val = False
            return bool(val)
