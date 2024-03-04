import FWCore.ParameterSet.Config as cms

def TriggerMatchEfficiencyPlotter(**kwargs):
  mod = cms.EDProducer('TriggerMatchEfficiencyPlotter',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
