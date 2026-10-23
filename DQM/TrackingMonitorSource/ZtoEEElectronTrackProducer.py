import FWCore.ParameterSet.Config as cms

def ZtoEEElectronTrackProducer(*args, **kwargs):
  mod = cms.EDProducer('ZtoEEElectronTrackProducer',
    electronInputTag = cms.untracked.InputTag('gedGsfElectrons'),
    offlineBeamSpot = cms.untracked.InputTag('offlineBeamSpot'),
    maxEta = cms.untracked.double(2.4),
    minPt = cms.untracked.double(5),
    maxDeltaPhiInEB = cms.untracked.double(0.15),
    maxDeltaEtaInEB = cms.untracked.double(0.007),
    maxHOEEB = cms.untracked.double(0.12),
    maxSigmaiEiEEB = cms.untracked.double(0.01),
    maxDeltaPhiInEE = cms.untracked.double(0.1),
    maxDeltaEtaInEE = cms.untracked.double(0.009),
    maxHOEEB_ = cms.untracked.double(0.1),
    maxSigmaiEiEEE = cms.untracked.double(0.03),
    maxNormChi2 = cms.untracked.double(10),
    maxD0 = cms.untracked.double(0.02),
    maxDz = cms.untracked.double(20),
    minPixelHits = cms.untracked.uint32(1),
    minStripHits = cms.untracked.uint32(8),
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
