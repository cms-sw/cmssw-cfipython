import FWCore.ParameterSet.Config as cms

def DQMSummaryPopConAnalyzer(*args, **kwargs):
  mod = cms.EDAnalyzer('DQMSummaryPopConAnalyzer',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
