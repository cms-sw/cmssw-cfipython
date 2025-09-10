import FWCore.ParameterSet.Config as cms

def DTRangeT0Print(*args, **kwargs):
  mod = cms.EDAnalyzer('DTRangeT0Print',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
