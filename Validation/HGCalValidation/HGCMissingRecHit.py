import FWCore.ParameterSet.Config as cms

def HGCMissingRecHit(*args, **kwargs):
  mod = cms.EDAnalyzer('HGCMissingRecHit',
    geometrySource = cms.vstring(
      'HGCalEESensitive',
      'HGCalHESiliconSensitive',
      'HGCalHEScintillatorSensitive'
    ),
    detectors = cms.vstring(
      'EE',
      'HE Silicon',
      'HE Scintillator'
    ),
    eeSimHitSource = cms.InputTag('g4SimHits', 'HGCHitsEE'),
    fhSimHitSource = cms.InputTag('g4SimHits', 'HGCHitsHEfront'),
    bhSimHitSource = cms.InputTag('g4SimHits', 'HGCHitsHEback'),
    eeDigiSource = cms.InputTag('simHGCalUnsuppressedDigis', 'EE'),
    fhDigiSource = cms.InputTag('simHGCalUnsuppressedDigis', 'HEfront'),
    bhDigiSource = cms.InputTag('simHGCalUnsuppressedDigis', 'HEback'),
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
