# HW3

1)Find the runtime of the algorithm mathematically (I should see summations). 
   Refer Qn1.png
   
2)Time this function for various n e.g. n = 1,2,3.... You should have small values of n all the way up to large values. Plot "time" vs "n" (time on y-axis and 
  n on x-axis). Also, fit a curve to your data, hint it's a polynomial.
  We timed the function over a range of n values, from tiny to huge, in order to determine how long the function f(n) takes. Plotting the data involved 
  placing the time taken on the y-axis and n on the x-axis.
  Interpreting Graphs:
  As n increases, the plot has a distinct quadratic trend, which reflects the O(n^2) complexity.

  A polynomial, more precisely a quadratic, that closely resembles the time data points is the fitted curve.
  
3)Find polynomials that are upper and lower bounds on your curve from #2. From this specify a big-O, a big-Omega, and what big-theta is 
 Big-O(Upper Bound): Slightly above the fitted curve, the green dashed line on the graph indicates the upper bound. This shows that O(n^2) is the upper bound 
 of the function.
 Big-Omega (Lower Bound) : The function is bounded below by Ω(n^2), as seen by the yellow dashed line that lies below the fitted curve.
 Big-Theta(Tight limit): The tight limit for the runtime is Θ(n^2) since the top and lower bounds are both quadratic and closely match the real timing data.


4) Find the approximate (eye ball it) location of "n_0" . Do this by zooming in on your plot and indicating on the plot where n_0 is and why you picked this value. Hint: I should see data that does not follow the trend of the polynomial you determined in #2

On the graph, a vertical dashed line at n=1800 indicates n0.
This value was selected because the empirical data points begin to closely match the quadratic trend at this point. Due to decreasing values of n, the data may exhibit greater fluctuation below n=1800n = 1800n=1800, sometimes resulting in overhead effects or discrepancies.
The measured performance is consistent with the projected n^2 complexity trend once n approaches and surpasses 1800.
The threshold denoted by n0 is the point at which the algorithm's performance is in consistent agreement with its asymptotic behavior. Variations caused by non-dominant factors may be more noticeable below this threshold, but the quadratic nature is dominant and dependable above this threshold. 

If I modified the function to be:
x = f(n)
   x = 1;
   y = 1;
   for i = 1:n
        for j = 1:n
             x = x + 1;
        y = i + j;


4) Will this increase how long it takes the algorithm to run (e.x. you are timing the function like in #2)?

Indeed, the additional action y = i + j; inside the inner loop of the changed code will cause it to execute a little bit faster. Nevertheless, this operation is a constant time operation O (1), and it does not alter the overall asymptotic complexity because it is performed n2n^2n2 times, the same number of times as the other operations inside the nested loops. Because of the extra operation, the adjusted function's time complexity will still be quadratic, or O(n^2), but with a somewhat bigger constant factor.
As can be seen from the blue data points on the graph, the changed function takes a little longer to complete than the original function, but it still follows the same general trend (quadratic).

5)Will it effect your results from #1?

No, as the operation is O(1), adding the line y = i + j; will not have an impact on the asymptotic notation of the findings from the runtime analysis. Runtime is still O(n^2). The updated and original routines both execute nested loops that run n×n=n^2 times, with a constant amount of time spent on each loop operation.
Particular Effect:
Upper Bound Big-O: Remains O(n^2).
Lower Bound Big-Omega: Retains Ω(n^2).
Tight Bound Big-Theta: Holds onto Θ(n^2).
This is seen in the graph, which confirms that the asymptotic behavior is identical since the fitted curve and bounds for the modified function still closely match a quadratic trend.



   
 




​
  

​
 
