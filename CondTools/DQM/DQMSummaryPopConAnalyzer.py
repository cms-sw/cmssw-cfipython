import FWCore.ParameterSet.Config as cms

def DQMSummaryPopConAnalyzer(**kwargs):
  mod = cms.EDAnalyzer('DQMSummaryPopConAnalyzer',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
