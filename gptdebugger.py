# GptDebugger module

def analyze_gpt_error(error_message):
    """Analyze a GPT error message and provide debugging suggestions"""
    error_types = {
        "connector": "This error occurs when GPT cannot communicate with the tool endpoint properly.",
        "rate limit": "This error occurs when too many requests are made in a short period.",
        "content filter": "This error occurs when content is flagged by the content moderation system.",
        "validation": "This error occurs when the input doesn't match the expected format."
    }
    
    suggestions = []
    detected_type = "unknown"
    
    # Analyze the error message
    if "connector" in error_message.lower():
        detected_type = "connector"
        suggestions = [
            "Check if the server is running and accessible",
            "Verify that the endpoint URL is correct",
            "Check if any network issues are preventing communication",
            "Examine API key permissions and validity"
        ]
    elif "rate limit" in error_message.lower() or "too many requests" in error_message.lower():
        detected_type = "rate_limit"
        suggestions = [
            "Implement exponential backoff in your requests",
            "Reduce the frequency of API calls",
            "Consider upgrading your API tier for higher limits",
            "Cache results when possible to reduce duplicate calls"
        ]
    elif "content filter" in error_message.lower() or "flagged" in error_message.lower():
        detected_type = "content_filter"
        suggestions = [
            "Review your prompts for potentially sensitive content",
            "Adjust phrasing to be more neutral",
            "Use alternate terminology that avoids triggering the filter",
            "Break complex requests into smaller, safer segments"
        ]
    elif "invalid" in error_message.lower() or "schema" in error_message.lower() or "parameter" in error_message.lower():
        detected_type = "validation"
        suggestions = [
            "Check the API documentation for correct parameter formats",
            "Ensure all required parameters are provided",
            "Verify that parameter types match the expected format",
            "Review error messages for specific validation failures"
        ]
    else:
        detected_type = "unknown"
        suggestions = [
            "Examine the full error message for additional context",
            "Check API documentation for this specific error",
            "Look for recent changes to the system that might have caused this",
            "Enable verbose logging to gather more information"
        ]
    
    return {
        "error_type": detected_type,
        "description": error_types.get(detected_type, "An unrecognized error type"),
        "suggestions": suggestions,
        "original_error": error_message
    }

# Main tool function that will be called
def run(params):
    """Main function for the GptDebugger tool"""
    error_message = params.get("error_message", "")
    if not error_message:
        return {
            "error": "Missing error_message parameter",
            "status": "failed"
        }
    
    # Analyze the error
    analysis = analyze_gpt_error(error_message)
    
    return {
        "analysis": analysis,
        "status": "success"
    }
