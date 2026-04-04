import FWCore.ParameterSet.Config as cms

def BooleanFlagFilter(*args, **kwargs):
  mod = cms.EDFilter('BooleanFlagFilter',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
