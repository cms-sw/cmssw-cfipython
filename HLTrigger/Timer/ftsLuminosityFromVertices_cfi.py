import FWCore.ParameterSet.Config as cms

ftsLuminosityFromVertices = cms.EDAnalyzer('FTSLuminosityFromVertices',
  source = cms.InputTag('siPixelClusters'),
  name = cms.string('vertices'),
  title = cms.string('reconstructed vertices'),
  label = cms.string('reconstructed vertices'),
  range = cms.double(40),
  resolution = cms.double(1)
)
