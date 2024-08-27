import FWCore.ParameterSet.Config as cms

def SiPixelFakeGainForHLTReader(**kwargs):
  mod = cms.EDAnalyzer('SiPixelFakeGainForHLTReader',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
