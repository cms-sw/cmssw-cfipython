import FWCore.ParameterSet.Config as cms

def HFNoseNoiseMapAnalyzer(*args, **kwargs):
  mod = cms.EDAnalyzer('HFNoseNoiseMapAnalyzer',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
