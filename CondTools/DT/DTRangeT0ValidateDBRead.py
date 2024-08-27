import FWCore.ParameterSet.Config as cms

def DTRangeT0ValidateDBRead(**kwargs):
  mod = cms.EDAnalyzer('DTRangeT0ValidateDBRead',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
