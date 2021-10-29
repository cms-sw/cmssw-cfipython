import FWCore.ParameterSet.Config as cms

hgcalRecHitMapProducer = cms.EDProducer('HGCalRecHitMapProducer',
  EEInput = cms.InputTag('HGCalRecHit', 'HGCEERecHits'),
  FHInput = cms.InputTag('HGCalRecHit', 'HGCHEFRecHits'),
  BHInput = cms.InputTag('HGCalRecHit', 'HGCHEBRecHits'),
  mightGet = cms.optional.untracked.vstring
)
