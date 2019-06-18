import FWCore.ParameterSet.Config as cms

PixelFEDChannelCollectionMapTestReader = cms.EDAnalyzer('PixelFEDChannelCollectionMapTestReader',
  printDebug = cms.untracked.bool(True),
  outputFile = cms.untracked.string(''),
  mightGet = cms.optional.untracked.vstring
)
