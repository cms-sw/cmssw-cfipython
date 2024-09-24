import FWCore.ParameterSet.Config as cms

def CSCSkim(*args, **kwargs):
  mod = cms.EDFilter('CSCSkim',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod