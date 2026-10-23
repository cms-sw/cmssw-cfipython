import FWCore.ParameterSet.Config as cms

def EcalDetailedTimeRecHitProducer(*args, **kwargs):
  mod = cms.EDProducer('EcalDetailedTimeRecHitProducer',
    EBRecHitCollection = cms.InputTag('ecalRecHit', 'EcalRecHitsEB'),
    EERecHitCollection = cms.InputTag('ecalRecHit', 'EcalRecHitsEE'),
    EBTimeDigiCollection = cms.InputTag('mix', 'EBTimeDigi'),
    EETimeDigiCollection = cms.InputTag('mix', 'EETimeDigi'),
    EBDetailedTimeRecHitCollection = cms.string('EcalRecHitsEB'),
    EEDetailedTimeRecHitCollection = cms.string('EcalRecHitsEE'),
    correctForVertexZPosition = cms.bool(False),
    useMCTruthVertex = cms.bool(False),
    recoVertex = cms.InputTag('offlinePrimaryVerticesWithBS'),
    simVertex = cms.InputTag('g4SimHits'),
    EBTimeLayer = cms.int32(7),
    EETimeLayer = cms.int32(3),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
