def api_return(plot_id, plot_memo, success: bool, err):
    if success:
        return {
            "plot_id": plot_id,
            "plot_memo": plot_memo,
            "success": True,
        }
    return {
        "data": err,
        "success": False,
    }
