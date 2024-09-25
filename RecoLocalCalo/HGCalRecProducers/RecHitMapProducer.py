import FWCore.ParameterSet.Config as cms

def RecHitMapProducer(*args, **kwargs):
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
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
