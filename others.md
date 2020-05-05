ransac implementation in CUDA and plot in python
https://github.com/cyd3r/ransac


EWMA IIR Filter
exponentially weighted moving average
https://en.wikipedia.org/wiki/Exponential_smoothing

    Camera's continuous auto-exposure/gain adjustment mechanism (enabled in state_func__connect_to_cameras()) seeks to
    respond to changes in scene lighting by dynamically tuning camera exposure and gain to trend captured image "gray value"
    towards a set target value ("TargetGrayValue" parameter), with the aim of producing images with a "nice" exposure level.
    
    Can calculate equivalent of auto-exposure adjustment process target value by calculating mean() of grayscale image.  When
    scene is steady auto-exposure adjustment process can be expected to modify camera exposure & gain so image "gray value"
    tracks towards and settles to steady state close to target.  If a change in scene with different lighting then occurs,
    will see a sudden jump (positive or negative) in "gray value", followed by it tracking back towards the target value under
    control of the adjustment process.
    
    Accordingly can use delta (rate of change over time) of the "gray value" as indicator of how good current exposure level.
    Experiments indicate that delta is a better indicator than absolule difference from "TargetGrayValue" as sometimes the
        auto-adjustment seems to settle on gain/exposure values that settle "gray value" close-ish but not at target.at
    Calculate mean/"gray value" in same AOI that auto-adjustment process is using
    
    It appears that the automatic exposure adjustment process is running on a relatively slow loop, such that even
    during an adjustment cycle can get subsequent images with same ExposureTime and therefore "grey value".  Similarly after
    a change of scene that results in a big step change of "grey value", can get several subsequent images with the same
    elevated value (and therefore no delta) before the adjustment process kicks in and starts tracking it back to target.
    Accordingly run the delta values through a simple low pass filter to average the deltas over the last few images.
    
    As want to detect step changes in "grey value" immediately (as they potentially correspond to images with poor exposure)
    perform asymmetric filtering such that any increase in <exposure_delta> is latched into the filter and reflected
    immediately in filter output, but decay back towards zero is filtered.
    
    if grey_delta > self._image_grey_value_delta_filter.get_value():
        self._image_grey_value_delta_filter.reset_to_steady_state(grey_delta)
    else:
        self._image_grey_value_delta_filter.add_sample(grey_delta)