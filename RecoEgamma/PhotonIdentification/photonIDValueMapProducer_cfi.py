import FWCore.ParameterSet.Config as cms

photonIDValueMapProducer = cms.EDProducer('PhotonIDValueMapProducer',
  particleBasedIsolation = cms.InputTag('particleBasedIsolation', 'gedPhotons'),
  src = cms.InputTag('gedPhotons'),
  srcMiniAOD = cms.InputTag('slimmedPhotons', '', '@skipCurrentProcess'),
  esReducedRecHitCollectionMiniAOD = cms.InputTag('reducedEgamma', 'reducedESRecHits'),
  eeReducedRecHitCollection = cms.InputTag('reducedEcalRecHitsEE'),
  pfCandidates = cms.InputTag('particleFlow'),
  vertices = cms.InputTag('offlinePrimaryVertices'),
  ebReducedRecHitCollectionMiniAOD = cms.InputTag('reducedEgamma', 'reducedEBRecHits'),
  eeReducedRecHitCollectionMiniAOD = cms.InputTag('reducedEgamma', 'reducedEERecHits'),
  esReducedRecHitCollection = cms.InputTag('reducedEcalRecHitsES'),
  pfCandidatesMiniAOD = cms.InputTag('packedPFCandidates'),
  verticesMiniAOD = cms.InputTag('offlineSlimmedPrimaryVertices'),
  ebReducedRecHitCollection = cms.InputTag('reducedEcalRecHitsEB')
)
