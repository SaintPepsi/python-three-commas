from py3cw.request import Py3CW
from ...model import *
from ...error import ThreeCommasError
from typing import Tuple


wrapper = Py3CW('', '')


def post():
    """
    /v2/smart_trades
    Create smart trade v2 (Permission: SMART_TRADE_WRITE, Security: SIGNED)

    """
    error, data = wrapper.request(
        entity='smart_trades_v2',
        action='new',
    )
    return ThreeCommasError(error), data


def patch_by_id(id):
    """
    /v2/smart_trades/{id}
    Update smart trade v2 (Permission: SMART_TRADE_WRITE, Security: SIGNED)

    """
    error, data = wrapper.request(
        entity='smart_trades_v2',
        action='update',
        action_id=str(id),
    )
    return ThreeCommasError(error), data


''' This endpoint was not present in the py3cw module
def post_reduce_funds_by_id(id):
    """
    /v2/smart_trades/{id}/reduce_funds
    Reduce funds for smart trade v2 (Permission: SMART_TRADE_WRITE, Security: SIGNED)

    """
    error, data = wrapper.request(
        entity='smart_trades_v2',
        action='<py3cw_action>',
        action_id=str(id),
    )
    return ThreeCommasError(error), data
'''


def post_add_funds_by_id(id):
    """
    /v2/smart_trades/{id}/add_funds
    Average for smart trade v2 (Permission: SMART_TRADE_WRITE, Security: SIGNED)

    """
    error, data = wrapper.request(
        entity='smart_trades_v2',
        action='add_funds',
        action_id=str(id),
    )
    return ThreeCommasError(error), data


def post_close_by_market_by_id(id):
    """
    /v2/smart_trades/{id}/close_by_market
    Close by market smart trade v2 (Permission: SMART_TRADE_WRITE, Security: SIGNED)

    """
    error, data = wrapper.request(
        entity='smart_trades_v2',
        action='close_by_market',
        action_id=str(id),
    )
    return ThreeCommasError(error), data


def post_force_start_by_id(id):
    """
    /v2/smart_trades/{id}/force_start
    Force start smart trade v2 (Permission: SMART_TRADE_WRITE, Security: SIGNED)

    """
    error, data = wrapper.request(
        entity='smart_trades_v2',
        action='force_start',
        action_id=str(id),
    )
    return ThreeCommasError(error), data


def post_force_process_by_id(id):
    """
    /v2/smart_trades/{id}/force_process
    Process smart trade v2 (Permission: SMART_TRADE_WRITE, Security: SIGNED)

    """
    error, data = wrapper.request(
        entity='smart_trades_v2',
        action='force_process',
        action_id=str(id),
    )
    return ThreeCommasError(error), data


def post_set_note_by_id(id):
    """
    /v2/smart_trades/{id}/set_note
    Set note to smart trade v2 (Permission: SMART_TRADE_WRITE, Security: SIGNED)

    """
    error, data = wrapper.request(
        entity='smart_trades_v2',
        action='set_note',
        action_id=str(id),
    )
    return ThreeCommasError(error), data


def get_trades_by_id(smart_trade_id):
    """
    /v2/smart_trades/{smart_trade_id}/trades
    Get smart trade v2 trades (Permission: SMART_TRADE_READ, Security: SIGNED)

    """
    error, data = wrapper.request(
        entity='smart_trades_v2',
        action='get_trades',
        action_id=str(smart_trade_id),
    )
    return ThreeCommasError(error), data


def post_trades_close_by_market_by_id(smart_trade_id, id):
    """
    /v2/smart_trades/{smart_trade_id}/trades/{id}/close_by_market
    Panic close trade by market (Permission: SMART_TRADE_WRITE, Security: SIGNED)

    """
    error, data = wrapper.request(
        entity='smart_trades_v2',
        action='panic_close_by_market',
        action_id=str(smart_trade_id),
        action_sub_id=str(id),
    )
    return ThreeCommasError(error), data


def delete_trades_by_id(smart_trade_id, id):
    """
    /v2/smart_trades/{smart_trade_id}/trades/{id}
    Cancel trade (Permission: SMART_TRADE_WRITE, Security: SIGNED)

    """
    error, data = wrapper.request(
        entity='smart_trades_v2',
        action='cancel_trade',
        action_id=str(smart_trade_id),
        action_sub_id=str(id),
    )
    return ThreeCommasError(error), data

