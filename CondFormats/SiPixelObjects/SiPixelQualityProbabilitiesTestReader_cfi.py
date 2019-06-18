import FWCore.ParameterSet.Config as cms

SiPixelQualityProbabilitiesTestReader = cms.EDAnalyzer('SiPixelQualityProbabilitiesTestReader',
  printDebug = cms.untracked.bool(True),
  outputFile = cms.untracked.string(''),
  mightGet = cms.optional.untracked.vstring
)
