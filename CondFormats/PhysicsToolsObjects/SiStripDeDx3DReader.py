import FWCore.ParameterSet.Config as cms

def SiStripDeDx3DReader(*args, **kwargs):
  mod = cms.EDAnalyzer('SiStripDeDx3DReader',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
