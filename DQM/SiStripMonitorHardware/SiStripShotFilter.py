import FWCore.ParameterSet.Config as cms

def SiStripShotFilter(*args, **kwargs):
  mod = cms.EDFilter('SiStripShotFilter',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
