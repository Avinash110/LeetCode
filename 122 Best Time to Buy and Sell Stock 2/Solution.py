class Solution:
	def maxProfit(self, prices):

		"""
		The idea behind solving this is buying the stock at every valley and selling the stock at every peak.

		So therefore let's assume a point A which is a valley and point D which is a peak and there are number of points
		between them. The profit will be buying the stock at A and selling at D which is (D-A). So for every valley we have to
		find the first peak after that point and take the difference and add that in profit.		
		
  	    i = 0
        valley = prices[0]
        peak = prices[0]
        maxprofit = 0
        while (i < prices.length - 1) 
            while (i < prices.length - 1 and prices[i] >= prices[i + 1]):
                i++
            valley = prices[i]
            while (i < prices.length - 1 and prices[i] <= prices[i + 1]):
                i++
            peak = prices[i]
            maxprofit += peak - valley
        return maxprofit


        Clever way doing this would be the following:
        1 - Suppose the valley is A and the peak is D and there are 2 point B,C in between them. We can just keep on
        adding the differences as we move along the path i.e. keep adding (B-A) + (C-B) + (D-C) which will eventually be 
        (D-A)
		"""
		profit = 0
        for i in range(1, len(prices)):
            if prices[i] > prices[i-1]:
                profit += prices[i]-prices[i-1]
        return profit