import logging
from datetime import datetime
import os
from utilities.otherutl import OtherUtlClass


class CustomLoggerClass:

    @staticmethod
    def check_log_file_folder_exist():
        now = datetime.now()
        # dd:mm:YY_H:M:S
        date = now.strftime("%d%m%Y")
        time = now.strftime("%H%M%S")
        today_folder_name = date
        other_utl_class = OtherUtlClass()
        path = os.path.join(other_utl_class.get_hkdl_folder_path() + "logs\\",
                            today_folder_name)

        print(f"path: {path}")
        print(f"today's date: {today_folder_name}")

        # check if the directory exist
        if not os.path.isdir(path):
            print("create a new directory")
            os.mkdir(path)

    @staticmethod
    def loggen():
        now = datetime.now()
        # dd:mm:YY_H:M:S
        date = now.strftime("%d%m%Y")
        time = now.strftime("%H%M%S")
        today_folder_name = date
        other_utl_class = OtherUtlClass()
        path = os.path.join(f'{other_utl_class.get_hkdl_folder_path()}logs\\',
                            today_folder_name)

        print(f"path: {path}")
        print(f"today's date: {today_folder_name}")

        # check if the directory exist
        if not os.path.isdir(path):
            print("create a new directory")
            os.mkdir(path)

        # show os
        cwd = os.getcwd()
        print(f"current working directory: {cwd}")
        cwd_split = cwd.split('/')
        print(f"total length of split string, {len(cwd_split)}")

        if len(cwd_split) < 5:
            cwd_split = cwd.split('\\')  # cater for windows where it will get cwd with \
            print(f"total length of split string ('\\'), {len(cwd_split)}")

        project_file_name = cwd_split[len(cwd_split) - 1]
        print(f"the file name is: {project_file_name}")

        print("basic config")
        logging.basicConfig(filename=f'logs/{today_folder_name}/hkdl_{project_file_name}_{time}.log',
                            level=logging.INFO,
                            force=True,
                            format='%(asctime)s: %(levelname)s: %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')
        logger = logging.getLogger()
        logger.setLevel(logging.INFO)
        return logger
