import FWCore.ParameterSet.Config as cms

def HcalL1TriggerObjectsPopConAnalyzer(**kwargs):
  mod = cms.EDAnalyzer('HcalL1TriggerObjectsPopConAnalyzer',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
