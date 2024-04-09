import FWCore.ParameterSet.Config as cms

def TotemTimingRecHitProducer(**kwargs):
  mod = cms.EDProducer('TotemTimingRecHitProducer',
    applyCalibration = cms.bool(False),
    timeSliceNs = cms.double(0),
    digiTag = cms.InputTag('totemTimingRawToDigi', 'TotemTiming'),
    timingCalibrationTag = cms.string('GlobalTag:TotemTimingCalibration'),
    baselinePoints = cms.int32(8),
    saturationLimit = cms.double(0.1),
    cfdFraction = cms.double(0.3),
    smoothingPoints = cms.int32(20),
    lowPassFrequency = cms.double(0.7),
    hysteresis = cms.double(0.005),
    mergeTimePeaks = cms.bool(True),
    sampicOffset = cms.double(1),
    sampicSamplingPeriodNs = cms.double(0.12995451591942819),
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod