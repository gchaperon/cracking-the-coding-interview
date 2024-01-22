project('cracking', 'cpp',
  version : '0.1',
  default_options : ['warning_level=3',
                     'cpp_std=c++14'])

catch_lib = subproject('catch2').get_variable('catch2_with_main_dep')
findresult = run_command('find', 'src', '-name', '[0-9][0-9]-*.cpp', check : true)
sourcenames = findresult.stdout().strip().split()

foreach sourcename : sourcenames
  parts = sourcename.split('/')
  chapter_index = parts[-2].substring(0, 2)
  problem_index = parts[-1].substring(0, 2)
  shortname = chapter_index + '-' + problem_index
  debug(sourcename, chapter_index, problem_index, shortname)

  exe = executable(shortname, [sourcename], dependencies : catch_lib)
  test(shortname, exe, verbose : true)
endforeach
