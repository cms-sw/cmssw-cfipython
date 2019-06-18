import FWCore.ParameterSet.Config as cms

SiPixelQualityProbabilitiesTestWriter = cms.EDAnalyzer('SiPixelQualityProbabilitiesTestWriter',
  printDebug = cms.untracked.bool(True),
  record = cms.string('SiPixelStatusScenarioProbabilityRcd'),
  snapshots = cms.string(''),
  probabilities = cms.string(''),
  mightGet = cms.optional.untracked.vstring
)
