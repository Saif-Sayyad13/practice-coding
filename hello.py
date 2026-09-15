'''for i in {1..100}
do
   git commit --allow-empty -m "Commit number $i"
done
git push origin main
'''
'''for i in {1..100}
do
   # Sets the date to October 15, 2025 at 12:00 PM
   export GIT_AUTHOR_DATE="2025-10-15T12:00:00"
   export GIT_COMMITTER_DATE="2025-10-15T12:00:00"
   git commit --allow-empty -m "Backdated commit $i"
done
git push origin main
'''