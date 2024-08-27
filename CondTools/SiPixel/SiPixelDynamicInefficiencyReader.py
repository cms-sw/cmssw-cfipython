import FWCore.ParameterSet.Config as cms

def SiPixelDynamicInefficiencyReader(**kwargs):
  mod = cms.EDAnalyzer('SiPixelDynamicInefficiencyReader',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
