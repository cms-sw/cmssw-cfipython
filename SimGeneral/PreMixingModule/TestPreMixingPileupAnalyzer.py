import FWCore.ParameterSet.Config as cms

def TestPreMixingPileupAnalyzer(*args, **kwargs):
  mod = cms.EDAnalyzer('TestPreMixingPileupAnalyzer',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
