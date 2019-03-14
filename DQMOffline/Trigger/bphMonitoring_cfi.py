import FWCore.ParameterSet.Config as cms

bphMonitoring = cms.EDAnalyzer('BPHMonitor',
  FolderName = cms.string('HLT/BPH/'),
  tracks = cms.InputTag('generalTracks'),
  offlinePVs = cms.InputTag('offlinePrimaryVertices'),
  beamSpot = cms.InputTag('offlineBeamSpot'),
  muons = cms.InputTag('muons'),
  muoSelection = cms.string('abs(eta)<1.4 & isPFMuon & isGlobalMuon  & innerTrack.hitPattern.trackerLayersWithMeasurement>5 & innerTrack.hitPattern.numberOfValidPixelHits>0'),
  muoSelection_ref = cms.string('isPFMuon & isGlobalMuon  & innerTrack.hitPattern.trackerLayersWithMeasurement>5 & innerTrack.hitPattern.numberOfValidPixelHits>0'),
  nmuons = cms.int32(1),
  numGenericTriggerEventPSet = cms.PSet(
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
  denGenericTriggerEventPSet = cms.PSet(
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
  histoPSet = cms.PSet(
    d0PSet = cms.PSet(),
    etaPSet = cms.PSet(),
    phiPSet = cms.PSet(),
    ptPSet = cms.PSet(),
    z0PSet = cms.PSet()
  )
)
