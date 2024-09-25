import FWCore.ParameterSet.Config as cms

def SiStripDeDx2DReader(*args, **kwargs):
  mod = cms.EDAnalyzer('SiStripDeDx2DReader',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
