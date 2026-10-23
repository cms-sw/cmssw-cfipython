import FWCore.ParameterSet.Config as cms

def DTT0ValidateDBWrite(*args, **kwargs):
  mod = cms.EDAnalyzer('DTT0ValidateDBWrite',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
