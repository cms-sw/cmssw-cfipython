import FWCore.ParameterSet.Config as cms

def TSToSimTSAssociatorByEnergyScoreProducer(**kwargs):
  mod = cms.EDProducer('TSToSimTSAssociatorByEnergyScoreProducer',
    hitMapTag = cms.InputTag('hgcalRecHitMapProducer'),
    hardScatterOnly = cms.bool(True),
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
