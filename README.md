# mysql-deadlock-expr

Simple experiment on reproducing deadlock on n concurrent transactions on MySQL.

deadlock-update is the time spent of updates with deadlock detection,
and normal-update is the measured time of updates without deadlock detection

Following figure shows the plot of deadlock-update and normal-update as n increases.

<div float="left" align="center">
    <img align="top" src="https://github.com/3-24/mysql-deadlock-expr/blob/main/plot.png?raw=true" alt="Plot" width="50%"/>
    <p>Cost of Deadlock Detection</p>
</div>
