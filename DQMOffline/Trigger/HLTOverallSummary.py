import FWCore.ParameterSet.Config as cms

def HLTOverallSummary(*args, **kwargs):
  mod = cms.EDAnalyzer('HLTOverallSummary',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
