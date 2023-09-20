import FWCore.ParameterSet.Config as cms

zeeDetails = cms.EDProducer('ZEEDetails',
  moduleName = cms.untracked.string('ZEEDetails'),
  folderName = cms.untracked.string('ElectronTracks'),
  electronInputTag = cms.untracked.InputTag('gedGsfElectrons'),
  offlineBeamSpot = cms.untracked.InputTag('offlineBeamSpot'),
  puTag = cms.untracked.InputTag('addPileupInfo'),
  vertexTag = cms.untracked.InputTag('offlinePrimaryVertices'),
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
  minInvMass = cms.untracked.double(60),
  maxInvMass = cms.untracked.double(120),
  trackQuality = cms.untracked.string('highPurity'),
  isMC = cms.untracked.bool(False),
  doPUCorrection = cms.untracked.bool(False),
  puScaleFactorFile = cms.untracked.string('PileupScaleFactor.root'),
  mightGet = cms.optional.untracked.vstring
)
