import FWCore.ParameterSet.Config as cms

def ErrorsPropagationAnalyzer(**kwargs):
  mod = cms.EDAnalyzer('ErrorsPropagationAnalyzer',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
