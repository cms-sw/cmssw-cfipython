import FWCore.ParameterSet.Config as cms

def DQMSummaryEventSetupAnalyzer(**kwargs):
  mod = cms.EDAnalyzer('DQMSummaryEventSetupAnalyzer',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
