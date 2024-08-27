import FWCore.ParameterSet.Config as cms

def HGCalShowerSeparation(**kwargs):
  mod = cms.EDProducer('HGCalShowerSeparation',
    debug = cms.int32(1),
    filterOnEnergyAndCaloP = cms.bool(False),
    caloParticles = cms.InputTag('mix', 'MergedCaloTruth'),
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
