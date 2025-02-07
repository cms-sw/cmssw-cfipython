import FWCore.ParameterSet.Config as cms

def SiPixelFEDChannelContainerTestReader(*args, **kwargs):
  mod = cms.EDAnalyzer('SiPixelFEDChannelContainerTestReader',
    printDebug = cms.untracked.bool(True),
    outputFile = cms.untracked.string(''),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
