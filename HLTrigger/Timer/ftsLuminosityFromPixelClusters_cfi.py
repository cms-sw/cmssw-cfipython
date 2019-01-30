import FWCore.ParameterSet.Config as cms

ftsLuminosityFromPixelClusters = cms.EDAnalyzer('FTSLuminosityFromPixelClusters',
  source = cms.InputTag('siPixelClusters'),
  name = cms.string('clusters'),
  title = cms.string('pixel clusters'),
  label = cms.string('pixel clusters'),
  range = cms.double(20000),
  resolution = cms.double(500)
)
