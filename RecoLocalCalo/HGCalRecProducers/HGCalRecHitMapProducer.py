import FWCore.ParameterSet.Config as cms

def HGCalRecHitMapProducer(**kwargs):
  mod = cms.EDProducer('HGCalRecHitMapProducer',
    EEInput = cms.InputTag('HGCalRecHit', 'HGCEERecHits'),
    FHInput = cms.InputTag('HGCalRecHit', 'HGCHEFRecHits'),
    BHInput = cms.InputTag('HGCalRecHit', 'HGCHEBRecHits'),
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
