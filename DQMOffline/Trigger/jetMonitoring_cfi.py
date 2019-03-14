import FWCore.ParameterSet.Config as cms

jetMonitoring = cms.EDAnalyzer('JetMonitor',
  FolderName = cms.string('HLT/Jet'),
  met = cms.InputTag('pfMet'),
  jetSrc = cms.InputTag('ak4PFJetsCHS'),
  electrons = cms.InputTag('gedGsfElectrons'),
  muons = cms.InputTag('muons'),
  njets = cms.int32(0),
  nelectrons = cms.int32(0),
  ptcut = cms.double(20),
  ispfjettrg = cms.bool(True),
  iscalojettrg = cms.bool(False),
  numGenericTriggerEventPSet = cms.PSet(
    dcsInputTag = cms.InputTag('scalersRawToDigi'),
    dcsPartitions = cms.vint32(),
    andOrDcs = cms.bool(False),
    errorReplyDcs = cms.bool(True),
    dbLabel = cms.string(''),
    andOrHlt = cms.bool(True),
    hltInputTag = cms.InputTag('TriggerResults', '', 'HLT'),
    hltPaths = cms.vstring(),
    errorReplyHlt = cms.bool(False),
    verbosityLevel = cms.uint32(1)
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
    errorReplyHlt = cms.bool(False),
    verbosityLevel = cms.uint32(1)
  ),
  histoPSet = cms.PSet(
    jetPSet = cms.PSet(),
    jetPtThrPSet = cms.PSet(),
    jetptBinning = cms.vdouble(
      0,
      20,
      40,
      60,
      80,
      90,
      100,
      110,
      120,
      130,
      140,
      150,
      160,
      170,
      180,
      190,
      200,
      220,
      240,
      260,
      280,
      300,
      350,
      400,
      450,
      1000
    ),
    lsPSet = cms.PSet(
      nbins = cms.uint32(2500)
    )
  )
)
