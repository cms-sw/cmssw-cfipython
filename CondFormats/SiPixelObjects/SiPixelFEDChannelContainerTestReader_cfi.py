import FWCore.ParameterSet.Config as cms

SiPixelFEDChannelContainerTestReader = cms.EDAnalyzer('SiPixelFEDChannelContainerTestReader',
  printDebug = cms.untracked.bool(True),
  outputFile = cms.untracked.string(''),
  mightGet = cms.optional.untracked.vstring
)
