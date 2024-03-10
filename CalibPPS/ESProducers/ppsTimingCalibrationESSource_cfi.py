import FWCore.ParameterSet.Config as cms

ppsTimingCalibrationESSource = cms.ESSource('PPSTimingCalibrationESSource',
  calibrationFile = cms.FileInPath(),
  subDetector = cms.uint32(0),
  appendToDataLabel = cms.string('')
)
