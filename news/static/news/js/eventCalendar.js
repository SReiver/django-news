(function($) {
    "use strict";
    $.fn.EventsCalendar = function(options) {
        Date.prototype.getDayFromMonday = function() {
            return this.getDay()?this.getDay():7;
        };

        Date.prototype.getMonthWeek = function() {
            var fd = new Date(this.getFullYear(), this.getMonth());
            return Math.ceil((((this - fd) / 86400000) + fd.getDayFromMonday()) / 7);
        };


        var settings = $.extend({
                defaultView: 'month',
                eventsList: false,
                ajaxUrl: false,
                updateEvents: false,
                fullEventTemplate: '<div><h3>__title__</h3><div>__image__</div><div>__date__</div><div>__content__</div></div>',
                dateFormat: {'year':'numeric','month':'long','day':'2-digit'}
            }, options),
            $this = this;

        $this.now = new Date();
        $this.year = $this.now.getFullYear();
        $this.month = $this.now.getMonth();
        $this.week = $this.now.getMonthWeek();
        $this.day = $this.now.getDayFromMonday();
        $this.events = {};

        if (!settings.ajaxUrl && !settings.eventsList) {
            $this.html('<div style="color:red;">Ошибка! Не указан источник данных!</div>');
            return $this;
        }

        function showFullEvent(block) {
            $(".fullView",$this).remove();
            var FVBlock = $("<div />",{
                    html:block.data("fullView"),
                    class:'fullView'
                }),
                closeBtn = $("<span />",{'class':'close-btn','text':'X'}).click(function(){
                    FVBlock.remove();
                }),
                position = block.position();
            FVBlock.css('top',position.top).css('left',position.left+80);
            $this.append(FVBlock.append(closeBtn));
        }

        function updateEventList(events){
            for (var i=0; i<events.length; i++){
                var event = events[i],
                    date = new Date(event['date']*1000),
                    year = date.getFullYear(),
                    month = date.getMonth(),
                    week = date.getMonthWeek(),
                    day = date.getDayFromMonday();
                if (!(year in $this.events))
                    $this.events[year]={};
                if (!(month in $this.events[year]))
                    $this.events[year][month]={};
                if (!(week in $this.events[year][month]))
                    $this.events[year][month][week]={};
                if (!(day in $this.events[year][month][week]))
                    $this.events[year][month][week][day]={};

                $this.events[year][month][week][day][event.id] = event;
            }
        }

        settings.eventsList && updateEventList(JSON.parse(settings.eventsList));

        function showEvents(year, month, week){
            var day = new Date(year, month, 1),
                first_day_num = day.getDayFromMonday(),
                last_day = new Date(year, month+1, 0),
                week_max = last_day.getMonthWeek(),
                monthEvents = year in $this.events ? month in $this.events[year] ? $this.events[year][month] : [] : [];
            $this.year = year;
            $this.month = month;
            $this.week = week;

            $this.find(".calendar-header .title").text(day.toLocaleString('ru-RU',{'year':'numeric','month':'long'}));

            for (var w=0; w<6; w++){
                var weekBlock = $this.find('.calendar-body .week').filter(":eq("+w+")"),
                    weekEvents = (w+1) in monthEvents? monthEvents[w+1]:{};

                if (week && (w+1)!=week){
                    weekBlock.hide();
                    continue;
                }
                weekBlock.show();
                if (w+1 > week_max)
                    weekBlock.hide();
                if (week)
                    weekBlock.addClass('singleweek');
                else
                    weekBlock.removeClass('singleweek');

                for (var d=1;d<8;d++){
                    var dayBlock = weekBlock.find(".day").filter(":eq("+(d-1)+")"),
                        dayTitle = dayBlock.find(".day-number"),
                        dayEventsBlock = dayBlock.find(".events"),
                        day_num = d+w*7-first_day_num+1,
                        date = new Date(year, month, day_num),
                        dayEvents = d in weekEvents?weekEvents[d]:[],
                        today = new Date();
                    dayEventsBlock.html('');
                    dayBlock.removeClass('current');
                    if (year==today.getFullYear() && month==today.getMonth() && w+1==today.getMonthWeek() && d==today.getDayFromMonday())
                        dayBlock.addClass('current');
                    dayTitle.text(date.getDate());
                    if (date.getMonth() == month)
                        dayTitle.addClass('current');
                    else
                        dayTitle.removeClass('current');
                    $.each(dayEvents, function(i,ev){
                        var evBlock = $("<div />",{'class':'event-item','title':ev.title}).text(ev.title),
                            eventTemplate = settings.fullEventTemplate;
                        for (var k in ev) {
                            if (k!='' && ev.hasOwnProperty(k)){
                                if (k=='date') {
                                    var evDate=new Date(ev[k]*1000);
                                    ev[k] = evDate.toLocaleString('ru-RU',settings.dateFormat);
                                }
                                eventTemplate = eventTemplate.replace("__"+k+"__",ev[k])
                            }
                        }
                        evBlock.data('fullView',eventTemplate);
                        evBlock.click(function () {
                           showFullEvent($(this));
                        });
                        dayEventsBlock.append(evBlock);
                    });
                }
            }
        }

        function getEvents(year, month, week) {
            if (settings.updateEvents || !(year in $this.events) || !(month in $this.events[year]) || ( week && !(week in $this.events[year][month]) )){
                var data = {'year':year, 'month':month};
                week && (data['week'] = week);
                $.getJSON(settings.ajaxUrl, data, function(answer){
                    if (answer.error == 0){
                        if (!settings.updateEvents && !(year in $this.events))
                            $this.events[year]={};
                        if (!settings.updateEvents && !(month in $this.events[year]))
                            $this.events[year][month]={};
                        if (!settings.updateEvents && (week && !(week in $this.events[year][month])))
                            $this.events[year][month][week]={};
                        updateEventList(answer.events);
                        showEvents(year, month, week);
                    }
                    else {
                        $this.html('<div style="color:red;">Ошибка при получении списка событий</div>');
                    }
                });
            }
            showEvents(year, month, week);
        }

        var CalendarHeader = $("<div />",{
            class:'calendar-header',
            html:'<div class="title"></div>'
        });
        var nextBtn = $("<span class='calendar-next'>></span>");
        var prevBtn = $("<span class='calendar-prev'><</span>");
        nextBtn.data('year',$this.year).data('month',$this.month).click(function(){
            $(".fullView",$this).remove();
            var month = $this.month+1,
                year = $this.year;
            if (month==12){
                year = year+1;
                month = 0;
            }
            getEvents(year,month);
        });
        prevBtn.data('year',$this.year).data('month',$this.month).click(function(){
            $(".fullView",$this).remove();
            var month = $this.month-1,
                year = $this.year;
            if (month==-1){
                year = year-1;
                month = 11;
            }
            getEvents(year,month);
        });
        CalendarHeader.append(nextBtn);
        CalendarHeader.prepend(prevBtn);
        var CalendarBody = $("<div />",{
            class:"calendar-body"
        });
        for (var w=0; w<6; w++){
            var weekBlock = $("<div />",{class:'week'});
            CalendarBody.append(weekBlock);
            for (var d=0; d<7; d++){
                var dayBlock = $("<div />",{
                    class:'day',
                    html:'<div class="day-number"></div><div class="events"></div>'
                });
                weekBlock.append(dayBlock);
            }
        }

        this.html(CalendarHeader).append(CalendarBody);
        getEvents($this.year,$this.month);

        return $this;
	}
})(jQuery);