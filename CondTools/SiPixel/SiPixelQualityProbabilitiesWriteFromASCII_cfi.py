import FWCore.ParameterSet.Config as cms

SiPixelQualityProbabilitiesWriteFromASCII = cms.EDAnalyzer('SiPixelQualityProbabilitiesWriteFromASCII',
  printDebug = cms.untracked.bool(True),
  record = cms.string('SiPixelStatusScenarioProbabilityRcd'),
  probabilities = cms.string(''),
  mightGet = cms.optional.untracked.vstring
)
