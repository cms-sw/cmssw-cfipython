import FWCore.ParameterSet.Config as cms

def SiPixelFakeGainForHLTReader(*args, **kwargs):
  mod = cms.EDAnalyzer('SiPixelFakeGainForHLTReader',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
