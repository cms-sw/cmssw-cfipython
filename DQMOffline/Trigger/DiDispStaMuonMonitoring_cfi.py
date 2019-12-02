import FWCore.ParameterSet.Config as cms

DiDispStaMuonMonitoring = cms.EDProducer('DiDispStaMuonMonitor',
  FolderName = cms.string('HLT/EXO/DiDispStaMuon'),
  muons = cms.InputTag('displacedStandAloneMuons'),
  nmuons = cms.uint32(2),
  muonSelection = cms.PSet(
    general = cms.string('pt > 0'),
    pt = cms.string(''),
    dxy = cms.string('pt > 0')
  ),
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
    muonDxyPSet = cms.PSet(
      nbins = cms.uint32(200),
      xmin = cms.double(-0.5),
      xmax = cms.double(19999.5)
    ),
    lsPSet = cms.PSet(
      nbins = cms.uint32(200),
      xmin = cms.double(-0.5),
      xmax = cms.double(19999.5)
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
