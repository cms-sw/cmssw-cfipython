import FWCore.ParameterSet.Config as cms

def L1TriggerScalerPopConAnalyzer(**kwargs):
  mod = cms.EDAnalyzer('L1TriggerScalerPopConAnalyzer',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
