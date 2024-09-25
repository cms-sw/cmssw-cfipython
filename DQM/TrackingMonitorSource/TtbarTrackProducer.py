import FWCore.ParameterSet.Config as cms

def TtbarTrackProducer(*args, **kwargs):
  mod = cms.EDProducer('TtbarTrackProducer',
    electronInputTag = cms.untracked.InputTag('gedGsfElectrons'),
    jetsInputTag = cms.untracked.InputTag('ak4PFJetsCHS'),
    bjetsInputTag = cms.untracked.InputTag('pfDeepCSVJetTags', 'probb'),
    pfmetTag = cms.untracked.InputTag('pfMet'),
    muonInputTag = cms.untracked.InputTag('muons'),
    offlineBeamSpot = cms.untracked.InputTag('offlineBeamSpot'),
    maxEtaEle = cms.untracked.double(2.4),
    maxEtaMu = cms.untracked.double(2.1),
    minPt = cms.untracked.double(5),
    maxDeltaPhiInEB = cms.untracked.double(0.15),
    maxDeltaEtaInEB = cms.untracked.double(0.007),
    maxHOEEB = cms.untracked.double(0.12),
    maxSigmaiEiEEB = cms.untracked.double(0.01),
    maxDeltaPhiInEE = cms.untracked.double(0.1),
    maxDeltaEtaInEE = cms.untracked.double(0.009),
    maxHOEEB_ = cms.untracked.double(0.1),
    maxSigmaiEiEEE = cms.untracked.double(0.03),
    minChambers = cms.untracked.uint32(2),
    minEta_Jets = cms.untracked.double(3),
    btagFactor = cms.untracked.double(0.6),
    maxNormChi2 = cms.untracked.double(10),
    maxD0 = cms.untracked.double(0.02),
    maxDz = cms.untracked.double(20),
    minPixelHits = cms.untracked.uint32(1),
    minStripHits = cms.untracked.uint32(8),
    maxIsoEle = cms.untracked.double(0.5),
    maxIsoMu = cms.untracked.double(0.3),
    minPtHighestMu = cms.untracked.double(24),
    minPtHighestEle = cms.untracked.double(32),
    minPtHighest_Jets = cms.untracked.double(30),
    minPt_Jets = cms.untracked.double(20),
    minInvMass = cms.untracked.double(140),
    maxInvMass = cms.untracked.double(200),
    minMet = cms.untracked.double(50),
    maxMet = cms.untracked.double(80),
    minWmass = cms.untracked.double(50),
    maxWmass = cms.untracked.double(130),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
