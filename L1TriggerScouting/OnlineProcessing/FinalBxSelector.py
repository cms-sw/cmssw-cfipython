import FWCore.ParameterSet.Config as cms

def FinalBxSelector(*args, **kwargs):
  mod = cms.EDFilter('FinalBxSelector',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
