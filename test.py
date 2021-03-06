import unittest
import os
from carbonaro import compile

# saves the list of directory names under tets/
directories = next(os.walk('tests'))[1]

def remove_empty_chunks_from_code(file_path):
    file = open(file_path, "r+")
    text = file.read()

    text = text.replace('\n\n', '')

    file.seek(0, os.SEEK_SET)
    file.write(text)
    file.close()


def prettify_and_read(file_path):
    remove_empty_chunks_from_code(file_path)

    os.system('clang-format -i -style=Microsoft {file_path}'.format(file_path=file_path))

    file = open(file_path)
    text = file.read()

    file.close()
    return text

def read_file(file_path):
    file = open(file_path)
    text = file.read()
    file.close()
    return text

class TestCarbonaro(unittest.TestCase):
    def test_general(self):
        for dir_name in directories:
            # read carb code and expected c code
            carb_code = read_file('./tests/{dir}/code.carb'.format(dir=dir_name))
            expected_c_code = prettify_and_read('./tests/{dir}/code.c'.format(dir=dir_name))

            # compiles carb code and saves it into out.c for every dir
            compile(carb_code, './tests/{dir}/out.c'.format(dir=dir_name))

            generated_c_code = prettify_and_read('./tests/{dir}/out.c'.format(dir=dir_name))

            # remove out.c
            os.remove('./tests/{dir}/out.c'.format(dir=dir_name))

            self.assertEqual(generated_c_code, expected_c_code, "`{dir}` test failed".format(dir=dir_name))

if __name__ == '__main__':
    unittest.main()
