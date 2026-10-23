import FWCore.ParameterSet.Config as cms

def L1ScoutingCaloTowerPhysicalValueMapProducer(*args, **kwargs):
  mod = cms.EDProducer('L1ScoutingCaloTowerPhysicalValueMapProducer',
    src = cms.required.InputTag,
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
