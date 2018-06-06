import FWCore.ParameterSet.Config as cms

totemTimingRecHits = cms.EDProducer('TotemTimingRecHitProducer',
  digiTag = cms.InputTag('totemTimingRawToDigi', 'TotemTiming'),
  calibrationFile = cms.string('/dev/null'),
  baselinePoints = cms.int32(8),
  saturationLimit = cms.double(0.85),
  cfdFraction = cms.double(0.5),
  smoothingPoints = cms.int32(20),
  lowPassFrequency = cms.double(0),
  hysteresis = cms.double(0.005)
)
