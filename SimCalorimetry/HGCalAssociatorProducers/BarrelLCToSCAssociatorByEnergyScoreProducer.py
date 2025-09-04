import FWCore.ParameterSet.Config as cms

def BarrelLCToSCAssociatorByEnergyScoreProducer(*args, **kwargs):
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
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
