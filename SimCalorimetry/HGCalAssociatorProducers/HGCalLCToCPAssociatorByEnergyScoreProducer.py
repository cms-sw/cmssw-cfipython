import FWCore.ParameterSet.Config as cms

def HGCalLCToCPAssociatorByEnergyScoreProducer(**kwargs):
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
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
