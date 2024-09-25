import FWCore.ParameterSet.Config as cms

def DTTtrigValidateDBRead(*args, **kwargs):
  mod = cms.EDAnalyzer('DTTtrigValidateDBRead',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
