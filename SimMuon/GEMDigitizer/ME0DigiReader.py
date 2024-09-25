import FWCore.ParameterSet.Config as cms

def ME0DigiReader(*args, **kwargs):
  mod = cms.EDAnalyzer('ME0DigiReader',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
