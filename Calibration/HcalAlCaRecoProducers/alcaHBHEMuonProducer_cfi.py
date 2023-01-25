import FWCore.ParameterSet.Config as cms

alcaHBHEMuonProducer = cms.EDProducer('AlCaHBHEMuonProducer',
  BeamSpotLabel = cms.InputTag('offlineBeamSpot'),
  VertexLabel = cms.InputTag('offlinePrimaryVertices'),
  EBRecHitLabel = cms.InputTag('ecalRecHit', 'EcalRecHitsEB'),
  EERecHitLabel = cms.InputTag('ecalRecHit', 'EcalRecHitsEE'),
  HBHERecHitLabel = cms.InputTag('hbhereco'),
  MuonLabel = cms.InputTag('muons'),
  MinimumMuonP = cms.double(5),
  mightGet = cms.optional.untracked.vstring
)
