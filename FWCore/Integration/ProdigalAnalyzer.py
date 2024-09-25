import FWCore.ParameterSet.Config as cms

def ProdigalAnalyzer(*args, **kwargs):
  mod = cms.EDAnalyzer('ProdigalAnalyzer',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
