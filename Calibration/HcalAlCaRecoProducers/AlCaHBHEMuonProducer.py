import FWCore.ParameterSet.Config as cms

def AlCaHBHEMuonProducer(**kwargs):
  mod = cms.EDProducer('AlCaHBHEMuonProducer',
    BeamSpotLabel = cms.InputTag('offlineBeamSpot'),
    VertexLabel = cms.InputTag('offlinePrimaryVertices'),
    EBRecHitLabel = cms.InputTag('ecalRecHit', 'EcalRecHitsEB'),
    EERecHitLabel = cms.InputTag('ecalRecHit', 'EcalRecHitsEE'),
    HBHERecHitLabel = cms.InputTag('hbhereco'),
    MuonLabel = cms.InputTag('muons'),
    MinimumMuonP = cms.double(5),
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
