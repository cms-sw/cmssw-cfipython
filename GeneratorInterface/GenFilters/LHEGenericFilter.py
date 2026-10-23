import FWCore.ParameterSet.Config as cms

def LHEGenericFilter(*args, **kwargs):
  mod = cms.EDFilter('LHEGenericFilter',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
