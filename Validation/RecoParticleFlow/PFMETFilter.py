import FWCore.ParameterSet.Config as cms

def PFMETFilter(*args, **kwargs):
  mod = cms.EDFilter('PFMETFilter',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
