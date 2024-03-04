import FWCore.ParameterSet.Config as cms

def EcalSeverityLevelAlgoAnalyzer(**kwargs):
  mod = cms.EDAnalyzer('EcalSeverityLevelAlgoAnalyzer',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
