import FWCore.ParameterSet.Config as cms

tau3muMonitoring = cms.EDProducer('Tau3MuMonitor',
  FolderName = cms.string('HLT/BPH/'),
  requireValidHLTPaths = cms.bool(True),
  taus = cms.InputTag('hltTauPt10MuPts511Mass1p2to2p3Iso', 'Taus'),
  histoPSet = cms.PSet(
    ptPSet = cms.PSet(
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
    massPSet = cms.PSet(
      nbins = cms.required.uint32,
      xmin = cms.required.double,
      xmax = cms.required.double
    )
  ),
  GenericTriggerEventPSet = cms.PSet(
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
  mightGet = cms.optional.untracked.vstring
)
