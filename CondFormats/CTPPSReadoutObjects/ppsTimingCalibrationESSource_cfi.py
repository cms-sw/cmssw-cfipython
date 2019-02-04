import FWCore.ParameterSet.Config as cms

ppsTimingCalibrationESSource = cms.ESSource('PPSTimingCalibrationESSource',
  calibrationFile = cms.FileInPath(''),
  appendToDataLabel = cms.string('')
)
