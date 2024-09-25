import FWCore.ParameterSet.Config as cms

def ScoutingTestAnalyzer(*args, **kwargs):
  mod = cms.EDProducer('ScoutingTestAnalyzer',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
