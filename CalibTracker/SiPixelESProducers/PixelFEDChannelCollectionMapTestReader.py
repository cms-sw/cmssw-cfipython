import FWCore.ParameterSet.Config as cms

def PixelFEDChannelCollectionMapTestReader(**kwargs):
  mod = cms.EDAnalyzer('PixelFEDChannelCollectionMapTestReader',
    printDebug = cms.untracked.bool(True),
    outputFile = cms.untracked.string(''),
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
