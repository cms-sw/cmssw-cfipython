import FWCore.ParameterSet.Config as cms

def SiPixelFakeGainOfflineReader(**kwargs):
  mod = cms.EDAnalyzer('SiPixelFakeGainOfflineReader',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
