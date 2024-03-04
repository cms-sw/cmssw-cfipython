import FWCore.ParameterSet.Config as cms

def SiPixelFEDChannelContainerTestReader(**kwargs):
  mod = cms.EDAnalyzer('SiPixelFEDChannelContainerTestReader',
    printDebug = cms.untracked.bool(True),
    outputFile = cms.untracked.string(''),
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
