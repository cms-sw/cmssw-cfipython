import FWCore.ParameterSet.Config as cms

def HltComparator(*args, **kwargs):
  mod = cms.EDFilter('HltComparator',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
