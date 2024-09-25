import FWCore.ParameterSet.Config as cms

def SiPixelDynamicInefficiencyDB(*args, **kwargs):
  mod = cms.EDAnalyzer('SiPixelDynamicInefficiencyDB',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
