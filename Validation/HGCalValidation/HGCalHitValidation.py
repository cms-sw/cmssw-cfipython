import FWCore.ParameterSet.Config as cms

def HGCalHitValidation(*args, **kwargs):
  mod = cms.EDProducer('HGCalHitValidation',
    geometrySource = cms.vstring(
      'HGCalEESensitive',
      'HGCalHESiliconSensitive',
      'HGCalHEScintillatorSensitive'
    ),
    eeSimHitSource = cms.InputTag('g4SimHits', 'HGCHitsEE'),
    fhSimHitSource = cms.InputTag('g4SimHits', 'HGCHitsHEfront'),
    bhSimHitSource = cms.InputTag('g4SimHits', 'HGCHitsHEback'),
    eeRecHitSource = cms.InputTag('HGCalRecHit', 'HGCEERecHits'),
    fhRecHitSource = cms.InputTag('HGCalRecHit', 'HGCHEFRecHits'),
    bhRecHitSource = cms.InputTag('HGCalRecHit', 'HGCHEBRecHits'),
    ietaExcludeBH = cms.vint32(),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
