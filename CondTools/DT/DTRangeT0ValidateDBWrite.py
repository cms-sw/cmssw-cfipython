import FWCore.ParameterSet.Config as cms

def DTRangeT0ValidateDBWrite(*args, **kwargs):
  mod = cms.EDAnalyzer('DTRangeT0ValidateDBWrite',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
