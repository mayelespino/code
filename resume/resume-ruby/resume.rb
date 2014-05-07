require 'yaml'

yml = YAML.load_file 'resume.yml'
yml['skills'].each { |skill|
    puts skill['skill']
}
yml['experience'].each { |position|
    puts position['position']
}

