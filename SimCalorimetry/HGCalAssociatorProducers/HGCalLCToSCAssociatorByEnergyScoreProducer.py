import FWCore.ParameterSet.Config as cms

def HGCalLCToSCAssociatorByEnergyScoreProducer(*args, **kwargs):
  mod = cms.EDProducer('HGCalLCToSCAssociatorByEnergyScoreProducer',
    hardScatterOnly = cms.bool(True),
    hitMapTag = cms.InputTag('recHitMapProducer', 'hgcalRecHitMap'),
    hits = cms.InputTag('recHitMapProducer', 'RefProdVectorHGCRecHitCollection'),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
