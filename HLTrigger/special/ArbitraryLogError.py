import FWCore.ParameterSet.Config as cms

def ArbitraryLogError(*args, **kwargs):
  mod = cms.EDAnalyzer('ArbitraryLogError',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
