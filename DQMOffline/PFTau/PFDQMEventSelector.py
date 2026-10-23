import FWCore.ParameterSet.Config as cms

def PFDQMEventSelector(*args, **kwargs):
  mod = cms.EDFilter('PFDQMEventSelector',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
