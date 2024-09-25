import FWCore.ParameterSet.Config as cms

def EcalSeverityLevelAlgoAnalyzer(*args, **kwargs):
  mod = cms.EDAnalyzer('EcalSeverityLevelAlgoAnalyzer',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
