import FWCore.ParameterSet.Config as cms

ppsTimingCalibrationLUTESSource = cms.ESSource('PPSTimingCalibrationLUTESSource',
  calibrationFile = cms.FileInPath(),
  appendToDataLabel = cms.string('')
)
