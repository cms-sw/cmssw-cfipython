import FWCore.ParameterSet.Config as cms

def RecHitMapProducer(**kwargs):
  mod = cms.EDProducer('RecHitMapProducer',
    EEInput = cms.InputTag('HGCalRecHit', 'HGCEERecHits'),
    FHInput = cms.InputTag('HGCalRecHit', 'HGCHEFRecHits'),
    BHInput = cms.InputTag('HGCalRecHit', 'HGCHEBRecHits'),
    EBInput = cms.InputTag('particleFlowRecHitECAL'),
    HBInput = cms.InputTag('particleFlowRecHitHBHE'),
    HOInput = cms.InputTag('particleFlowRecHitHO'),
    hgcalOnly = cms.bool(True),
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
