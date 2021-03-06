import FWCore.ParameterSet.Config as cms

trackToTrackComparisonHists = cms.EDProducer('TrackToTrackComparisonHists',
  requireValidHLTPaths = cms.bool(True),
  monitoredTrack = cms.InputTag('hltMergedTracks'),
  monitoredBeamSpot = cms.InputTag('hltOnlineBeamSpot'),
  monitoredPrimaryVertices = cms.InputTag('hltVerticesPFSelector'),
  referenceTrack = cms.InputTag('generalTracks'),
  referenceBeamSpot = cms.InputTag('offlineBeamSpot'),
  referencePrimaryVertices = cms.InputTag('offlinePrimaryVertices'),
  topDirName = cms.string('HLT/Tracking/ValidationWRTOffline'),
  dRmin = cms.double(0.002),
  pTCutForPlateau = cms.double(0.9),
  dxyCutForPlateau = cms.double(2.5),
  dzWRTPvCut = cms.double(1000000),
  genericTriggerEventPSet = cms.PSet(
    andOr = cms.bool(False),
    dcsInputTag = cms.InputTag('scalersRawToDigi'),
    dcsPartitions = cms.vint32(
      24,
      25,
      26,
      27,
      28,
      29
    ),
    andOrDcs = cms.bool(False),
    errorReplyDcs = cms.bool(True),
    dbLabel = cms.string(''),
    andOrHlt = cms.bool(True),
    hltInputTag = cms.InputTag('TriggerResults', '', 'HLT'),
    hltPaths = cms.vstring(),
    hltDBKey = cms.string(''),
    errorReplyHlt = cms.bool(False),
    verbosityLevel = cms.uint32(1)
  ),
  histoPSet = cms.PSet(
    Eta_rangeMin = cms.double(-2.5),
    Eta_rangeMax = cms.double(2.5),
    Eta_nbin = cms.uint32(50),
    Pt_rangeMin = cms.double(0.1),
    Pt_rangeMax = cms.double(100),
    Pt_nbin = cms.uint32(1000),
    Phi_rangeMin = cms.double(-3.1416),
    Phi_rangeMax = cms.double(3.1416),
    Phi_nbin = cms.uint32(36),
    Dxy_rangeMin = cms.double(-1),
    Dxy_rangeMax = cms.double(1),
    Dxy_nbin = cms.uint32(300),
    Dz_rangeMin = cms.double(-30),
    Dz_rangeMax = cms.double(30),
    Dz_nbin = cms.uint32(60),
    ptRes_rangeMin = cms.double(-0.1),
    ptRes_rangeMax = cms.double(0.1),
    ptRes_nbin = cms.uint32(100),
    phiRes_rangeMin = cms.double(-0.01),
    phiRes_rangeMax = cms.double(0.01),
    phiRes_nbin = cms.uint32(300),
    etaRes_rangeMin = cms.double(-0.01),
    etaRes_rangeMax = cms.double(0.01),
    etaRes_nbin = cms.uint32(300),
    dxyRes_rangeMin = cms.double(-0.05),
    dxyRes_rangeMax = cms.double(0.05),
    dxyRes_nbin = cms.uint32(500),
    dzRes_rangeMin = cms.double(-0.05),
    dzRes_rangeMax = cms.double(0.05),
    dzRes_nbin = cms.uint32(150)
  ),
  mightGet = cms.optional.untracked.vstring
)
