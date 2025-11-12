import FWCore.ParameterSet.Config as cms

def BarrelPCToCPAssociatorByEnergyScoreProducer(*args, **kwargs):
  mod = cms.EDProducer('BarrelPCToCPAssociatorByEnergyScoreProducer',
    hardScatterOnly = cms.bool(True),
    hitMapTag = cms.InputTag('recHitMapProducer', 'barrelRecHitMap'),
    hits = cms.InputTag('recHitMapProducer', 'RefProdVectorPFRecHitCollection'),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
