import FWCore.ParameterSet.Config as cms

def DTRangeT0Write(**kwargs):
  mod = cms.EDAnalyzer('DTRangeT0Write',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
