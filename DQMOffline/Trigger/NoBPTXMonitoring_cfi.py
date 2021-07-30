import FWCore.ParameterSet.Config as cms

NoBPTXMonitoring = cms.EDProducer('NoBPTXMonitor',
  FolderName = cms.string('HLT/NoBPTX'),
  requireValidHLTPaths = cms.bool(True),
  jets = cms.InputTag('ak4CaloJets'),
  muons = cms.InputTag('displacedStandAloneMuons'),
  jetSelection = cms.string('pt > 0'),
  muonSelection = cms.string('pt > 0'),
  njets = cms.uint32(0),
  nmuons = cms.uint32(0),
  numGenericTriggerEventPSet = cms.PSet(
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
    verbosityLevel = cms.uint32(1)
  ),
  denGenericTriggerEventPSet = cms.PSet(
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
    verbosityLevel = cms.uint32(1)
  ),
  histoPSet = cms.PSet(
    jetEPSet = cms.PSet(
      nbins = cms.required.uint32,
      xmin = cms.required.double,
      xmax = cms.required.double
    ),
    jetEtaPSet = cms.PSet(
      nbins = cms.required.uint32,
      xmin = cms.required.double,
      xmax = cms.required.double
    ),
    jetPhiPSet = cms.PSet(
      nbins = cms.required.uint32,
      xmin = cms.required.double,
      xmax = cms.required.double
    ),
    muonPtPSet = cms.PSet(
      nbins = cms.required.uint32,
      xmin = cms.required.double,
      xmax = cms.required.double
    ),
    muonEtaPSet = cms.PSet(
      nbins = cms.required.uint32,
      xmin = cms.required.double,
      xmax = cms.required.double
    ),
    muonPhiPSet = cms.PSet(
      nbins = cms.required.uint32,
      xmin = cms.required.double,
      xmax = cms.required.double
    ),
    lsPSet = cms.PSet(
      nbins = cms.required.uint32,
      xmin = cms.required.double,
      xmax = cms.required.double
    ),
    bxPSet = cms.PSet(
      nbins = cms.uint32(2500),
      xmin = cms.double(0),
      xmax = cms.double(2500)
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
  ),
  mightGet = cms.optional.untracked.vstring
)
