import FWCore.ParameterSet.Config as cms

def DQMSummaryEventSetupAnalyzer(*args, **kwargs):
  mod = cms.EDAnalyzer('DQMSummaryEventSetupAnalyzer',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
