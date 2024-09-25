import FWCore.ParameterSet.Config as cms

def SiPixelVCalReader(*args, **kwargs):
  mod = cms.EDAnalyzer('SiPixelVCalReader',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
