import FWCore.ParameterSet.Config as cms

def AlCaHBHEMuonProducer(*args, **kwargs):
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
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
