import FWCore.ParameterSet.Config as cms

def MultiClusterAssociatorByEnergyScoreProducer(**kwargs):
  mod = cms.EDProducer('MultiClusterAssociatorByEnergyScoreProducer',
    hitMapTag = cms.InputTag('hgcalRecHitMapProducer'),
    hardScatterOnly = cms.bool(True),
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
