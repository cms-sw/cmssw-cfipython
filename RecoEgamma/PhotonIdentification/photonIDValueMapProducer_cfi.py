import FWCore.ParameterSet.Config as cms

photonIDValueMapProducer = cms.EDProducer('PhotonIDValueMapProducer',
  particleBasedIsolation = cms.InputTag('particleBasedIsolation', 'gedPhotons'),
  src = cms.InputTag('slimmedPhotons', '', '@skipCurrentProcess'),
  esReducedRecHitCollection = cms.InputTag('reducedEgamma', 'reducedESRecHits'),
  ebReducedRecHitCollection = cms.InputTag('reducedEgamma', 'reducedEBRecHits'),
  eeReducedRecHitCollection = cms.InputTag('reducedEgamma', 'reducedEERecHits'),
  pfCandidates = cms.InputTag('packedPFCandidates'),
  vertices = cms.InputTag('offlineSlimmedPrimaryVertices'),
  isAOD = cms.bool(False)
)
