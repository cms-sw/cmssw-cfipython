import FWCore.ParameterSet.Config as cms

def HcalDcsValuesPopConAnalyzer(*args, **kwargs):
  mod = cms.EDAnalyzer('HcalDcsValuesPopConAnalyzer',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
