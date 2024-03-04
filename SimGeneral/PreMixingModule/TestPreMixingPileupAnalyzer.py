import FWCore.ParameterSet.Config as cms

def TestPreMixingPileupAnalyzer(**kwargs):
  mod = cms.EDAnalyzer('TestPreMixingPileupAnalyzer',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
