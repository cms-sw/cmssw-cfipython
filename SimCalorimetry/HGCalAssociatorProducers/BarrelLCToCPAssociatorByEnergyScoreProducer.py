import FWCore.ParameterSet.Config as cms

def BarrelLCToCPAssociatorByEnergyScoreProducer(**kwargs):
  mod = cms.EDProducer('BarrelLCToCPAssociatorByEnergyScoreProducer',
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
