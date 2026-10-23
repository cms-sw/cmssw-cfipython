import FWCore.ParameterSet.Config as cms

def HGCalRecHitValidation(*args, **kwargs):
  mod = cms.EDProducer('HGCalRecHitValidation',
    DetectorName = cms.string('HGCalEESensitive'),
    RecHitSource = cms.InputTag('HGCalRecHit', 'HGCEERecHits'),
    Verbosity = cms.untracked.int32(0),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
