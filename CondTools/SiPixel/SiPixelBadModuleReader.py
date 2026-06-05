import FWCore.ParameterSet.Config as cms

def SiPixelBadModuleReader(*args, **kwargs):
  mod = cms.EDAnalyzer('SiPixelBadModuleReader',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
