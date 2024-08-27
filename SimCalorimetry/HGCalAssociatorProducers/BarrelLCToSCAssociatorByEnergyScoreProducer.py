import FWCore.ParameterSet.Config as cms

def BarrelLCToSCAssociatorByEnergyScoreProducer(**kwargs):
  mod = cms.EDProducer('BarrelLCToSCAssociatorByEnergyScoreProducer',
    hardScatterOnly = cms.bool(True),
    hitMapTag = cms.InputTag('recHitMapProducer', 'barrelRecHitMap'),
    hits = cms.VInputTag(
      'particleFlowRecHitECAL',
      'particleFlowRecHitHBHE',
      'particleFlowRecHitHO'
    ),
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
