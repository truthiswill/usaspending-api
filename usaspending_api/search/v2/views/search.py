from rest_framework.response import Response
from rest_framework.views import APIView

from collections import OrderedDict

from usaspending_api.common.exceptions import InvalidParameterException
from usaspending_api.awards.v2.filters.transaction import transaction_filter
import ast
from usaspending_api.common.helpers import generate_fiscal_year, generate_fiscal_period, generate_fiscal_month

import logging
logger = logging.getLogger(__name__)


class SpendingOverTimeVisualizationViewSet(APIView):

    def post(self, request):
        """Return all budget function/subfunction titles matching the provided search text"""
        json_request = request.data
        group = json_request.get('group', None)
        filters = json_request.get('filters', None)

        if group is None:
            raise InvalidParameterException('Missing one or more required request parameters: group')
        if filters is None:
            raise InvalidParameterException('Missing one or more required request parameters: filters')
        potential_groups = ["quarter", "fiscal_year", "month", "fy", "q", "m"]
        if group not in potential_groups:
            raise InvalidParameterException('group does not have a valid value')

        queryset = transaction_filter(filters)
        # Filter based on search text
        response = {'group': group, 'results': []}

        # filter queryset by time
        group_results = OrderedDict()  # list of time_period objects ie {"fy": "2017", "quarter": "3"} : 1000
        queryset = queryset.order_by("action_date").values("action_date", "federal_action_obligation")
        for trans in queryset:
            key = {}
            if group == "fy" or group == "fiscal_year":
                fy = generate_fiscal_year(trans["action_date"])
                key = {"fiscal_year": str(fy)}
            elif group == "m" or group == 'month':
                fy = generate_fiscal_year(trans["action_date"])
                m = generate_fiscal_month(trans["action_date"])
                key = {"fiscal_year": str(fy), "month": str(m)}
            else:  # quarter
                fy = generate_fiscal_year(trans["action_date"])
                q = generate_fiscal_period(trans["action_date"])
                key = {"fiscal_year": str(fy), "quarter": str(q)}
            key = str(key)
            if group_results.get(key) is None:
                group_results[key] = trans["federal_action_obligation"]
            else:
                if trans["federal_action_obligation"]:
                    group_results[key] = group_results.get(key) + trans["federal_action_obligation"]
                else:
                    group_results[key] = group_results.get(key)

        results = []
        # Expected results structure
        # [{
        # "time_period": {"fy": "2017", "quarter": "3"},
        # 	"aggregated_amount": "200000000"
        # }]
        for key, value in group_results.items():
            key_dict = ast.literal_eval(key)
            result = {"time_period": key_dict, "aggregated_amount": float(value)}
            results.append(result)
        response['results'] = results

        return Response(response)