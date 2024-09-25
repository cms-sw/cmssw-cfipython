import FWCore.ParameterSet.Config as cms

def TriggerMatchEfficiencyPlotter(*args, **kwargs):
  mod = cms.EDProducer('TriggerMatchEfficiencyPlotter',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
