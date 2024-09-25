import FWCore.ParameterSet.Config as cms

def SiStripBFieldFilter(*args, **kwargs):
  mod = cms.EDFilter('SiStripBFieldFilter',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
