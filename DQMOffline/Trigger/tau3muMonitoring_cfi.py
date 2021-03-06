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
    andOr = cms.required.bool,
    dcsInputTag = cms.InputTag('scalersRawToDigi'),
    dcsPartitions = cms.vint32(),
    andOrDcs = cms.bool(False),
    errorReplyDcs = cms.bool(True),
    dbLabel = cms.string(''),
    andOrHlt = cms.bool(True),
    hltInputTag = cms.InputTag('TriggerResults', '', 'HLT'),
    hltPaths = cms.vstring(),
    hltDBKey = cms.string(''),
    errorReplyHlt = cms.bool(False),
    verbosityLevel = cms.uint32(0)
  ),
  mightGet = cms.optional.untracked.vstring
)
