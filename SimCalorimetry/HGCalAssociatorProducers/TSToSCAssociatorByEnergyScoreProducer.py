import FWCore.ParameterSet.Config as cms

def TSToSCAssociatorByEnergyScoreProducer(**kwargs):
  mod = cms.EDProducer('TSToSCAssociatorByEnergyScoreProducer',
    hitMapTag = cms.InputTag('hgcalRecHitMapProducer'),
    hardScatterOnly = cms.bool(True),
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
