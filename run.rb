require 'beeminder'

def main()
    bee = Beeminder::User.new token
    bee.goals.each do |goal|
        puts goal
        puts goal.losedate
        puts goal.datapublic
        puts goal.secret
        puts goal.slug # goalname
        puts goal.title # description
        puts
    end
end
  
def token
    return File.new("token.secret").read.strip
end

main()