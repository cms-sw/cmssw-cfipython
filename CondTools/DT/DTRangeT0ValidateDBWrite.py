import FWCore.ParameterSet.Config as cms

def DTRangeT0ValidateDBWrite(**kwargs):
  mod = cms.EDAnalyzer('DTRangeT0ValidateDBWrite',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
