import FWCore.ParameterSet.Config as cms

def SiStripCommissioningRunTypeFilter(*args, **kwargs):
  mod = cms.EDFilter('SiStripCommissioningRunTypeFilter',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
