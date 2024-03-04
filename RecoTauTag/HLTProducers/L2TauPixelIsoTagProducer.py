import FWCore.ParameterSet.Config as cms

def L2TauPixelIsoTagProducer(**kwargs):
  mod = cms.EDProducer('L2TauPixelIsoTagProducer',
    JetSrc = cms.InputTag('hltL2DiTauCaloJets'),
    BeamSpotSrc = cms.InputTag('hltOnlineBeamSpot'),
    VertexSrc = cms.InputTag('hltPixelVertices'),
    MaxNumberPV = cms.int32(1),
    IsoConeMax = cms.double(0.4),
    IsoConeMin = cms.double(0.2),
    TrackMinPt = cms.double(1.6),
    TrackMinNHits = cms.int32(3),
    TrackMaxNChi2 = cms.double(100),
    TrackPVMaxDZ = cms.double(0.1),
    TrackMaxDxy = cms.double(0.2),
    TrackSrc = cms.InputTag(''),
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
