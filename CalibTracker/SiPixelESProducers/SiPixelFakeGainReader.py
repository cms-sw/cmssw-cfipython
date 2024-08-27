import FWCore.ParameterSet.Config as cms

def SiPixelFakeGainReader(**kwargs):
  mod = cms.EDAnalyzer('SiPixelFakeGainReader',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
