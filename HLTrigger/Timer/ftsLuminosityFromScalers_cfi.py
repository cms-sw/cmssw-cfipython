import FWCore.ParameterSet.Config as cms

ftsLuminosityFromScalers = cms.EDAnalyzer('FTSLuminosityFromScalers',
  source = cms.InputTag('scalersRawToDigi'),
  type = cms.string('InstantaneousLuminosity'),
  name = cms.string('luminosity'),
  title = cms.string('instantaneous luminosity'),
  label = cms.string('instantaneous luminosity [cm^{-2}s^{-1}]'),
  range = cms.double(8e+33),
  resolution = cms.double(1e+31)
)
