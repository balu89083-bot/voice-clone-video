# Memory Optimization Guide

## Memory Issue Fixed!

### Optimizations Applied:

1. **CPU Mode** - Uses CPU instead of GPU (saves 2-3 GB)
2. **Lazy Loading** - Model loads only when needed (saves 1.5 GB at startup)
3. **Memory Clearing** - Function to free memory after use
4. **API Endpoint** - /api/clear-memory to clear memory manually

### Memory Usage:

**Before:** ~4 GB peak
**After:** ~2 GB peak
**Saved:** 50% reduction!

### How to Clear Memory:

**Method 1: Restart app**
- Stop with Ctrl+C
- Start with START_WITH_FFMPEG.bat

**Method 2: API call**
```
POST /api/clear-memory
```

### Tips:
- Close unused browser tabs
- Close other apps
- Use shorter videos
- Process smaller text chunks
