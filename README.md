# mysql-deadlock-expr

Simple experiment on reproducing deadlock on n concurrent transactions on MySQL.

deadlock-update is the time spent of updates with deadlock detection,
and normal-update is the measured time of updates without deadlock detection
