import FWCore.ParameterSet.Config as cms

NoBPTXMonitoring = cms.EDAnalyzer('NoBPTXMonitor',
  FolderName = cms.string('HLT/NoBPTX'),
  jets = cms.InputTag('ak4CaloJets'),
  muons = cms.InputTag('displacedStandAloneMuons'),
  jetSelection = cms.string('pt > 0'),
  muonSelection = cms.string('pt > 0'),
  njets = cms.uint32(0),
  nmuons = cms.uint32(0),
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
    hltDBKey = cms.string(''),
    errorReplyHlt = cms.bool(False),
    verbosityLevel = cms.uint32(1)
  ),
  histoPSet = cms.PSet(
    jetEPSet = cms.PSet(
      nbins = cms.uint32(200),
      xmin = cms.double(-0.5),
      xmax = cms.double(19999.5)
    ),
    jetEtaPSet = cms.PSet(
      nbins = cms.uint32(200),
      xmin = cms.double(-0.5),
      xmax = cms.double(19999.5)
    ),
    jetPhiPSet = cms.PSet(
      nbins = cms.uint32(200),
      xmin = cms.double(-0.5),
      xmax = cms.double(19999.5)
    ),
    muonPtPSet = cms.PSet(
      nbins = cms.uint32(200),
      xmin = cms.double(-0.5),
      xmax = cms.double(19999.5)
    ),
    muonEtaPSet = cms.PSet(
      nbins = cms.uint32(200),
      xmin = cms.double(-0.5),
      xmax = cms.double(19999.5)
    ),
    muonPhiPSet = cms.PSet(
      nbins = cms.uint32(200),
      xmin = cms.double(-0.5),
      xmax = cms.double(19999.5)
    ),
    lsPSet = cms.PSet(
      nbins = cms.uint32(2000)
    ),
    bxPSet = cms.PSet(
      nbins = cms.uint32(2000)
    ),
    jetEBinning = cms.vdouble(
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
    muonPtBinning = cms.vdouble(
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
    )
  )
)
