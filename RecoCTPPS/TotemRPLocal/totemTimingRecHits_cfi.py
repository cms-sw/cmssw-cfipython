import FWCore.ParameterSet.Config as cms

totemTimingRecHits = cms.EDProducer('TotemTimingRecHitProducer',
  digiTag = cms.InputTag('totemTimingRawToDigi', 'TotemTiming'),
  calibrationFile = cms.FileInPath('RecoCTPPS/TotemRPLocal/data/timing_offsets_ufsd_2018.dec18.cal.json'),
  baselinePoints = cms.int32(8),
  saturationLimit = cms.double(0.85),
  cfdFraction = cms.double(0.3),
  smoothingPoints = cms.int32(20),
  lowPassFrequency = cms.double(0.7),
  hysteresis = cms.double(0.005),
  mergeTimePeaks = cms.bool(True)
)
