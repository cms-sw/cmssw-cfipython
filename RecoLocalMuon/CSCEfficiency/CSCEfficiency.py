import FWCore.ParameterSet.Config as cms

def CSCEfficiency(*args, **kwargs):
  mod = cms.EDFilter('CSCEfficiency',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
