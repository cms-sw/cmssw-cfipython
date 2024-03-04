import FWCore.ParameterSet.Config as cms

def HGCalRecHitValidation(**kwargs):
  mod = cms.EDProducer('HGCalRecHitValidation',
    DetectorName = cms.string('HGCalEESensitive'),
    RecHitSource = cms.InputTag('HGCalRecHit', 'HGCEERecHits'),
    Verbosity = cms.untracked.int32(0),
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
