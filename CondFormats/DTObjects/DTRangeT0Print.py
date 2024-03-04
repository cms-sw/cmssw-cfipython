import FWCore.ParameterSet.Config as cms

def DTRangeT0Print(**kwargs):
  mod = cms.EDAnalyzer('DTRangeT0Print',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
