import FWCore.ParameterSet.Config as cms

def DTRangeT0ValidateDBRead(*args, **kwargs):
  mod = cms.EDAnalyzer('DTRangeT0ValidateDBRead',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
