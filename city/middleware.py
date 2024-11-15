import datetime

class TrackUserVisitsMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        session = request.session
        current_date = datetime.date.today().isoformat()

        if 'visit_history' not in session:
            session['visit_history'] = {}

        visit_history = session['visit_history']

        if current_date in visit_history:
            visit_history[current_date] += 1
        else:
            visit_history[current_date] = 1

        session['visit_history'] = visit_history

        response = self.get_response(request)
        return response
