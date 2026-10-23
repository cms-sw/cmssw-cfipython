import FWCore.ParameterSet.Config as cms

def SiPixelDynamicInefficiencyReader(*args, **kwargs):
  mod = cms.EDAnalyzer('SiPixelDynamicInefficiencyReader',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
