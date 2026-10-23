import FWCore.ParameterSet.Config as cms

def BPHMonitor(*args, **kwargs):
  mod = cms.EDProducer('BPHMonitor',
    FolderName = cms.string('HLT/BPH/'),
    requireValidHLTPaths = cms.bool(True),
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
    l1GtRecordInputTag = cms.InputTag(''),
    l1GtReadoutRecordInputTag = cms.InputTag(''),
    l1GtTriggerMenuLiteInputTag = cms.InputTag(''),
    l1tAlgBlkInputTag = cms.InputTag('gtStage2Digis'),
    l1tExtBlkInputTag = cms.InputTag('gtStage2Digis'),
    ReadPrescalesFromFile = cms.bool(False),
    numGenericTriggerEventPSet = cms.PSet(
      ReadPrescalesFromFile = cms.bool(False),
      andOr = cms.bool(False),
      andOrDcs = cms.bool(False),
      andOrHlt = cms.bool(False),
      andOrL1 = cms.bool(False),
      errorReplyDcs = cms.bool(False),
      errorReplyHlt = cms.bool(False),
      errorReplyL1 = cms.bool(False),
      l1BeforeMask = cms.bool(False),
      stage2 = cms.bool(False),
      dcsInputTag = cms.InputTag('scalersRawToDigi'),
      dcsRecordInputTag = cms.InputTag('onlineMetaDataDigis'),
      hltInputTag = cms.InputTag('TriggerResults', '', 'HLT'),
      l1tAlgBlkInputTag = cms.InputTag('gtStage2Digis'),
      l1tExtBlkInputTag = cms.InputTag('gtStage2Digis'),
      dbLabel = cms.string(''),
      hltDBKey = cms.string(''),
      dcsPartitions = cms.vint32(),
      hltPaths = cms.vstring(),
      l1Algorithms = cms.vstring(),
      verbosityLevel = cms.uint32(0)
    ),
    denGenericTriggerEventPSet = cms.PSet(
      ReadPrescalesFromFile = cms.bool(False),
      andOr = cms.bool(False),
      andOrDcs = cms.bool(False),
      andOrHlt = cms.bool(False),
      andOrL1 = cms.bool(False),
      errorReplyDcs = cms.bool(False),
      errorReplyHlt = cms.bool(False),
      errorReplyL1 = cms.bool(False),
      l1BeforeMask = cms.bool(False),
      stage2 = cms.bool(False),
      dcsInputTag = cms.InputTag('scalersRawToDigi'),
      dcsRecordInputTag = cms.InputTag('onlineMetaDataDigis'),
      hltInputTag = cms.InputTag('TriggerResults', '', 'HLT'),
      l1tAlgBlkInputTag = cms.InputTag('gtStage2Digis'),
      l1tExtBlkInputTag = cms.InputTag('gtStage2Digis'),
      dbLabel = cms.string(''),
      hltDBKey = cms.string(''),
      dcsPartitions = cms.vint32(),
      hltPaths = cms.vstring(),
      l1Algorithms = cms.vstring(),
      verbosityLevel = cms.uint32(0)
    ),
    histoPSet = cms.PSet(
      ptBinning = cms.vdouble(
        -0.5,
        0,
        2,
        4,
        8,
        10,
        12,
        16,
        20,
        25,
        30,
        35,
        40,
        50
      ),
      dMuPtBinning = cms.vdouble(
        6,
        8,
        12,
        16,
        20,
        25,
        30,
        35,
        40,
        50,
        70
      ),
      probBinning = cms.vdouble(
        0.01,
        0.02,
        0.04,
        0.06,
        0.08,
        0.1,
        0.2,
        0.3,
        0.4,
        0.5,
        0.6,
        0.7,
        0.8,
        0.9,
        1
      ),
      d0PSet = cms.PSet(
        nbins = cms.required.uint32,
        xmin = cms.required.double,
        xmax = cms.required.double
      ),
      etaPSet = cms.PSet(
        nbins = cms.required.uint32,
        xmin = cms.required.double,
        xmax = cms.required.double
      ),
      phiPSet = cms.PSet(
        nbins = cms.required.uint32,
        xmin = cms.required.double,
        xmax = cms.required.double
      ),
      z0PSet = cms.PSet(
        nbins = cms.required.uint32,
        xmin = cms.required.double,
        xmax = cms.required.double
      ),
      dRPSet = cms.PSet(
        nbins = cms.required.uint32,
        xmin = cms.required.double,
        xmax = cms.required.double
      ),
      massPSet = cms.PSet(
        nbins = cms.required.uint32,
        xmin = cms.required.double,
        xmax = cms.required.double
      ),
      BmassPSet = cms.PSet(
        nbins = cms.required.uint32,
        xmin = cms.required.double,
        xmax = cms.required.double
      ),
      dcaPSet = cms.PSet(
        nbins = cms.required.uint32,
        xmin = cms.required.double,
        xmax = cms.required.double
      ),
      dsPSet = cms.PSet(
        nbins = cms.required.uint32,
        xmin = cms.required.double,
        xmax = cms.required.double
      ),
      cosPSet = cms.PSet(
        nbins = cms.required.uint32,
        xmin = cms.required.double,
        xmax = cms.required.double
      )
    ),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
