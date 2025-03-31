from typing import Optional
import opencc

class TextConverter:
    """
    Handles conversion between Traditional and Simplified Chinese characters.
    Uses OpenCC library for accurate character conversion.
    """
    
    def __init__(self):
        self._converter = opencc.OpenCC('t2s.json')
    
    def to_simplified(self, text: str) -> str:
        """
        Converts Traditional Chinese characters to Simplified Chinese.
        
        Args:
            text (str): Text containing Traditional Chinese characters
            
        Returns:
            str: Text converted to Simplified Chinese characters
        """
        if not text:
            return ""
        return self._converter.convert(text)
    
    def clean_text(self, text: str) -> Optional[str]:
        """
        Cleans and normalizes Chinese text by:
        - Converting to Simplified Chinese
        - Removing extra whitespace
        - Handling any invalid characters
        
        Args:
            text (str): Input text to clean
            
        Returns:
            Optional[str]: Cleaned text, or None if text is invalid
        """
        try:
            if not text:
                return None
                
            simplified = self.to_simplified(text)
            
            cleaned = " ".join(simplified.split())
            
            return cleaned if cleaned else None
            
        except Exception as e:
            print(f"Error cleaning text: {str(e)}")
            return None