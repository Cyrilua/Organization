from employee_data import EmployeeDATA


class SpecialSerializer:
    @staticmethod
    def write(organization_dict, file):
        for key in organization_dict:
            file.write('key$#' + key + '\n')
            for empl in organization_dict[key]:
                file.write(
                    'empl$#' + empl.fullname + '#' + empl.post + '#' + empl.birth_year + '#' + empl.payment + '\n')
            file.write('end_of_key$#\n')

    @staticmethod
    def load(file):
        result = {}
        current_key = None
        for line in file:
            split_line = line.rstrip('\n').split('#')
            if split_line[0] == 'key$':
                current_key = split_line[1]
                result.update({current_key: []})
                continue
            if split_line[0] == 'empl$':
                new_empl_data = EmployeeDATA()
                new_empl_data.fullname = split_line[1]
                new_empl_data.post = split_line[2]
                new_empl_data.birth_year = split_line[3]
                new_empl_data.payment = split_line[4]
                result[current_key].append(new_empl_data)
                continue
            if split_line[0] == 'end_of_key$':
                current_key = None
                continue

        return result