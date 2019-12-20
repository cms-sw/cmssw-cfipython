import FWCore.ParameterSet.Config as cms

bphMonitoring = cms.EDProducer('BPHMonitor',
  FolderName = cms.string('HLT/BPH/'),
  tracks = cms.InputTag('generalTracks'),
  photons = cms.InputTag('photons'),
  offlinePVs = cms.InputTag('offlinePrimaryVertices'),
  beamSpot = cms.InputTag('offlineBeamSpot'),
  muons = cms.InputTag('muons'),
  hltTriggerSummaryAOD = cms.InputTag('hltTriggerSummaryAOD', '', 'HLT'),
  muoSelection = cms.string(''),
  muoSelection_ref = cms.string('isPFMuon & isGlobalMuon  & innerTrack.hitPattern.trackerLayersWithMeasurement>5 & innerTrack.hitPattern.numberOfValidPixelHits> 0'),
  muoSelection_tag = cms.string('isGlobalMuon && isPFMuon && isTrackerMuon && abs(eta) < 2.4 && innerTrack.hitPattern.numberOfValidPixelHits > 0 && innerTrack.hitPattern.trackerLayersWithMeasurement > 5 && globalTrack.hitPattern.numberOfValidMuonHits > 0 && globalTrack.normalizedChi2 < 10'),
  muoSelection_probe = cms.string('isPFMuon & isGlobalMuon  & innerTrack.hitPattern.trackerLayersWithMeasurement>5 & innerTrack.hitPattern.numberOfValidPixelHits> 0'),
  trSelection_ref = cms.string(''),
  DMSelection_ref = cms.string('Pt>4 & abs(eta)'),
  nmuons = cms.int32(1),
  tnp = cms.bool(False),
  L3 = cms.int32(0),
  ptCut = cms.int32(0),
  displaced = cms.int32(0),
  trOrMu = cms.int32(0),
  Jpsi = cms.int32(0),
  Upsilon = cms.int32(0),
  enum = cms.int32(1),
  seagull = cms.int32(1),
  maxmass = cms.double(3.596),
  minmass = cms.double(2.596),
  maxmassJpsi = cms.double(3.2),
  minmassJpsi = cms.double(3),
  maxmassUpsilon = cms.double(10),
  minmassUpsilon = cms.double(8.8),
  maxmassTkTk = cms.double(10),
  minmassTkTk = cms.double(0),
  maxmassJpsiTk = cms.double(5.46),
  minmassJpsiTk = cms.double(5.1),
  kaon_mass = cms.double(0.493677),
  mu_mass = cms.double(0.1056583745),
  min_dR = cms.double(0.001),
  max_dR = cms.double(1.4),
  minprob = cms.double(0.005),
  mincos = cms.double(0.95),
  minDS = cms.double(3),
  stageL1Trigger = cms.uint32(1),
  numGenericTriggerEventPSet = cms.PSet(
    andOr = cms.required.bool,
    dcsInputTag = cms.InputTag('scalersRawToDigi'),
    hltInputTag = cms.InputTag('TriggerResults', '', 'HLT'),
    dcsPartitions = cms.vint32(),
    andOrDcs = cms.bool(False),
    errorReplyDcs = cms.bool(True),
    dbLabel = cms.string(''),
    andOrHlt = cms.bool(True),
    andOrL1 = cms.bool(True),
    hltPaths = cms.vstring(),
    l1Algorithms = cms.vstring(),
    hltDBKey = cms.string(''),
    errorReplyHlt = cms.bool(False),
    errorReplyL1 = cms.bool(True),
    l1BeforeMask = cms.bool(True),
    verbosityLevel = cms.uint32(0)
  ),
  denGenericTriggerEventPSet = cms.PSet(
    andOr = cms.required.bool,
    dcsInputTag = cms.InputTag('scalersRawToDigi'),
    hltInputTag = cms.InputTag('TriggerResults', '', 'HLT'),
    dcsPartitions = cms.vint32(),
    andOrDcs = cms.bool(False),
    errorReplyDcs = cms.bool(True),
    dbLabel = cms.string(''),
    andOrHlt = cms.bool(True),
    andOrL1 = cms.bool(True),
    hltPaths = cms.vstring(),
    l1Algorithms = cms.vstring(),
    hltDBKey = cms.string(''),
    errorReplyHlt = cms.bool(False),
    errorReplyL1 = cms.bool(True),
    l1BeforeMask = cms.bool(True),
    verbosityLevel = cms.uint32(0)
  ),
  histoPSet = cms.PSet(
    d0PSet = cms.PSet(
      nbins = cms.required.int32,
      xmin = cms.required.double,
      xmax = cms.required.double
    ),
    etaPSet = cms.PSet(
      nbins = cms.required.int32,
      xmin = cms.required.double,
      xmax = cms.required.double
    ),
    phiPSet = cms.PSet(
      nbins = cms.required.int32,
      xmin = cms.required.double,
      xmax = cms.required.double
    ),
    ptPSet = cms.PSet(
      nbins = cms.required.int32,
      xmin = cms.required.double,
      xmax = cms.required.double
    ),
    dMu_ptPSet = cms.PSet(
      nbins = cms.required.int32,
      xmin = cms.required.double,
      xmax = cms.required.double
    ),
    z0PSet = cms.PSet(
      nbins = cms.required.int32,
      xmin = cms.required.double,
      xmax = cms.required.double
    ),
    dRPSet = cms.PSet(
      nbins = cms.required.int32,
      xmin = cms.required.double,
      xmax = cms.required.double
    ),
    massPSet = cms.PSet(
      nbins = cms.required.int32,
      xmin = cms.required.double,
      xmax = cms.required.double
    ),
    BmassPSet = cms.PSet(
      nbins = cms.required.int32,
      xmin = cms.required.double,
      xmax = cms.required.double
    ),
    dcaPSet = cms.PSet(
      nbins = cms.required.int32,
      xmin = cms.required.double,
      xmax = cms.required.double
    ),
    dsPSet = cms.PSet(
      nbins = cms.required.int32,
      xmin = cms.required.double,
      xmax = cms.required.double
    ),
    cosPSet = cms.PSet(
      nbins = cms.required.int32,
      xmin = cms.required.double,
      xmax = cms.required.double
    ),
    probPSet = cms.PSet(
      nbins = cms.required.int32,
      xmin = cms.required.double,
      xmax = cms.required.double
    )
  ),
  mightGet = cms.optional.untracked.vstring
)
