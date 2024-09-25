import FWCore.ParameterSet.Config as cms

def TSToSCAssociatorByEnergyScoreProducer(*args, **kwargs):
  mod = cms.EDProducer('TSToSCAssociatorByEnergyScoreProducer',
    hitMapTag = cms.InputTag('recHitMapProducer', 'hgcalRecHitMap'),
    hits = cms.VInputTag(
      'HGCalRecHit:HGCEERecHits',
      'HGCalRecHit:HGCHEFRecHits',
      'HGCalRecHit:HGCHEBRecHits'
    ),
    hardScatterOnly = cms.bool(True),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
