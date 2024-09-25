import FWCore.ParameterSet.Config as cms

def BarrelLCToCPAssociatorByEnergyScoreProducer(*args, **kwargs):
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
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
