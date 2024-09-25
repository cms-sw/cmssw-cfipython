import FWCore.ParameterSet.Config as cms

def DTT0ValidateDBRead(*args, **kwargs):
  mod = cms.EDAnalyzer('DTT0ValidateDBRead',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
