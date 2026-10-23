import FWCore.ParameterSet.Config as cms

def ZtoMMMuonTrackProducer(*args, **kwargs):
  mod = cms.EDProducer('ZtoMMMuonTrackProducer',
    muonInputTag = cms.untracked.InputTag('muons'),
    offlineBeamSpot = cms.untracked.InputTag('offlineBeamSpot'),
    maxEta = cms.untracked.double(2.4),
    minPt = cms.untracked.double(5),
    maxNormChi2 = cms.untracked.double(1000),
    maxD0 = cms.untracked.double(0.02),
    maxDz = cms.untracked.double(20),
    minPixelHits = cms.untracked.uint32(1),
    minStripHits = cms.untracked.uint32(8),
    minChambers = cms.untracked.uint32(2),
    minMatches = cms.untracked.uint32(2),
    minMatchedStations = cms.untracked.double(2),
    maxIso = cms.untracked.double(0.3),
    minPtHighest = cms.untracked.double(24),
    minInvMass = cms.untracked.double(75),
    maxInvMass = cms.untracked.double(105),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
