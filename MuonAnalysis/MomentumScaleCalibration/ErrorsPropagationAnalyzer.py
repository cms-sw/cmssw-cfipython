import FWCore.ParameterSet.Config as cms

def ErrorsPropagationAnalyzer(*args, **kwargs):
  mod = cms.EDAnalyzer('ErrorsPropagationAnalyzer',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
