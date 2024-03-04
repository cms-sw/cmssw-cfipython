import FWCore.ParameterSet.Config as cms

def PhotonIDValueMapProducer(**kwargs):
  mod = cms.EDProducer('PhotonIDValueMapProducer',
    particleBasedIsolation = cms.InputTag('particleBasedIsolation', 'gedPhotons'),
    src = cms.InputTag('slimmedPhotons', '', '@skipCurrentProcess'),
    esReducedRecHitCollection = cms.InputTag('reducedEgamma', 'reducedESRecHits'),
    ebReducedRecHitCollection = cms.InputTag('reducedEgamma', 'reducedEBRecHits'),
    eeReducedRecHitCollection = cms.InputTag('reducedEgamma', 'reducedEERecHits'),
    pfCandidates = cms.InputTag('packedPFCandidates'),
    vertices = cms.InputTag('offlineSlimmedPrimaryVertices'),
    isAOD = cms.bool(False),
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
