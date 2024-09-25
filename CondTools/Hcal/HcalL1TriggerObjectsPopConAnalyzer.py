import FWCore.ParameterSet.Config as cms

def HcalL1TriggerObjectsPopConAnalyzer(*args, **kwargs):
  mod = cms.EDAnalyzer('HcalL1TriggerObjectsPopConAnalyzer',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
