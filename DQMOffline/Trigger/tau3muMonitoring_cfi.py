import FWCore.ParameterSet.Config as cms

tau3muMonitoring = cms.EDAnalyzer('Tau3MuMonitor',
  FolderName = cms.string('HLT/BPH/'),
  taus = cms.InputTag('hltTauPt10MuPts511Mass1p2to2p3Iso', 'Taus'),
  histoPSet = cms.PSet(
    ptPSet = cms.PSet(),
    etaPSet = cms.PSet(),
    phiPSet = cms.PSet(),
    massPSet = cms.PSet()
  ),
  GenericTriggerEventPSet = cms.PSet(
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
  )
)
