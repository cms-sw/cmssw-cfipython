import FWCore.ParameterSet.Config as cms

def DetIdToRecHitMapProducer(*args, **kwargs):
  mod = cms.EDProducer('DetIdToRecHitMapProducer',
    hgcalRecHits = cms.VInputTag(
      'HGCalRecHit:HGCEERecHits',
      'HGCalRecHit:HGCHEFRecHits',
      'HGCalRecHit:HGCHEBRecHits'
    ),
    pfRecHits = cms.VInputTag(
      'particleFlowRecHitECAL:Cleaned',
      'particleFlowRecHitHBHE:Cleaned',
      'particleFlowRecHitHF:Cleaned',
      'particleFlowRecHitHO:Cleaned'
    ),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
