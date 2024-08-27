import FWCore.ParameterSet.Config as cms

def SiPixelDynamicInefficiencyDB(**kwargs):
  mod = cms.EDAnalyzer('SiPixelDynamicInefficiencyDB',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
