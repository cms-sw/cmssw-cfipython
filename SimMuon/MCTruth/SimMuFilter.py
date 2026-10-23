import FWCore.ParameterSet.Config as cms

def SimMuFilter(*args, **kwargs):
  mod = cms.EDFilter('SimMuFilter',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
