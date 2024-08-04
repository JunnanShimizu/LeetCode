class Solution:
    def reformatDate(self, date: str) -> str:
        length = len(date)
        
        months = {"Jan":"01", "Feb":"02", "Mar":"03", "Apr":"04", "May":"05", 
                  "Jun":"06", "Jul":"07", "Aug":"08", "Sep":"09", "Oct":"10", "Nov":"11", "Dec":"12"}
        
        day = date[0 : length - 11]
        
        if len(day) == 1:
            day = "0" + day
        
        return date[length - 4:length] + "-" + months.get(date[length - 8 : length - 5]) + "-" + day