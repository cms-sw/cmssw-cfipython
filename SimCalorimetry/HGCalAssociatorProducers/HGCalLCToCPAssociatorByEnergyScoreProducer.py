import FWCore.ParameterSet.Config as cms

def HGCalLCToCPAssociatorByEnergyScoreProducer(*args, **kwargs):
  mod = cms.EDProducer('HGCalLCToCPAssociatorByEnergyScoreProducer',
    hardScatterOnly = cms.bool(True),
    hitMapTag = cms.InputTag('recHitMapProducer', 'hgcalRecHitMap'),
    hits = cms.VInputTag(
      'HGCalRecHit:HGCEERecHits',
      'HGCalRecHit:HGCHEFRecHits',
      'HGCalRecHit:HGCHEBRecHits'
    ),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
