import FWCore.ParameterSet.Config as cms

def RecHitFlatTableProducer(*args, **kwargs):
  mod = cms.EDProducer('RecHitFlatTableProducer',
    objName = cms.string('rechits'),
    label_rechits = cms.VInputTag(
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
