import FWCore.ParameterSet.Config as cms

def BarrelTSToSimTSHitLCAssociatorByEnergyScoreProducer(*args, **kwargs):
  mod = cms.EDProducer('BarrelTSToSimTSHitLCAssociatorByEnergyScoreProducer',
    hitMapTag = cms.InputTag('recHitMapProducer', 'barrelRecHitMap'),
    hits = cms.VInputTag(
      'particleFlowRecHitECAL',
      'particleFlowRecHitHBHE'
    ),
    hardScatterOnly = cms.bool(True),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
