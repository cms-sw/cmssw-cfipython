import FWCore.ParameterSet.Config as cms

def HGCHitValidation(**kwargs):
  mod = cms.EDAnalyzer('HGCHitValidation',
    makeTree = cms.untracked.bool(True),
    geometrySource = cms.untracked.vstring(
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
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
