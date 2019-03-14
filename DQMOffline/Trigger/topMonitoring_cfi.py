import FWCore.ParameterSet.Config as cms

topMonitoring = cms.EDAnalyzer('TopMonitor',
  FolderName = cms.string('HLT/TOP'),
  met = cms.InputTag('pfMet'),
  jets = cms.InputTag('ak4PFJetsCHS'),
  electrons = cms.InputTag('gedGsfElectrons'),
  muons = cms.InputTag('muons'),
  vertices = cms.InputTag('offlinePrimaryVertices'),
  btagalgo = cms.InputTag('pfCombinedSecondaryVertexV2BJetTags'),
  metSelection = cms.string('pt > 0'),
  jetSelection = cms.string('pt > 0'),
  eleSelection = cms.string('pt > 0'),
  muoSelection = cms.string('pt > 0'),
  HTdefinition = cms.string('pt > 0'),
  vertexSelection = cms.string('!isFake'),
  bjetSelection = cms.string('pt > 0'),
  njets = cms.uint32(0),
  nelectrons = cms.uint32(0),
  nmuons = cms.uint32(0),
  leptJetDeltaRmin = cms.double(0),
  bJetMuDeltaRmax = cms.double(9999),
  bJetDeltaEtaMax = cms.double(9999),
  HTcut = cms.double(0),
  nbjets = cms.uint32(0),
  workingpoint = cms.double(0.8484),
  applyleptonPVcuts = cms.bool(False),
  invMassUppercut = cms.double(-1),
  invMassLowercut = cms.double(-1),
  oppositeSignMuons = cms.bool(False),
  MHTdefinition = cms.string('pt > 0'),
  MHTcut = cms.double(-1),
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
    metPSet = cms.PSet(),
    etaPSet = cms.PSet(),
    phiPSet = cms.PSet(),
    ptPSet = cms.PSet(),
    htPSet = cms.PSet(),
    DRPSet = cms.PSet(),
    csvPSet = cms.PSet(),
    invMassPSet = cms.PSet(),
    MHTPSet = cms.PSet(),
    metBinning = cms.vdouble(
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
    HTBinning = cms.vdouble(
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
    jetPtBinning = cms.vdouble(
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
    elePtBinning = cms.vdouble(
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
    muPtBinning = cms.vdouble(
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
    jetEtaBinning = cms.vdouble(
      -3,
      -2.5,
      -2,
      -1.5,
      -1,
      -0.5,
      0,
      0.5,
      1,
      1.5,
      2,
      2.5,
      3
    ),
    eleEtaBinning = cms.vdouble(
      -3,
      -2.5,
      -2,
      -1.5,
      -1,
      -0.5,
      0,
      0.5,
      1,
      1.5,
      2,
      2.5,
      3
    ),
    muEtaBinning = cms.vdouble(
      -3,
      -2.5,
      -2,
      -1.5,
      -1,
      -0.5,
      0,
      0.5,
      1,
      1.5,
      2,
      2.5,
      3
    ),
    invMassVariableBinning = cms.vdouble(
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
    MHTVariableBinning = cms.vdouble(
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
    HTBinning2D = cms.vdouble(
      0,
      40,
      80,
      100,
      120,
      140,
      160,
      180,
      200,
      240,
      280,
      350,
      450,
      1000
    ),
    jetPtBinning2D = cms.vdouble(
      0,
      40,
      80,
      100,
      120,
      140,
      160,
      180,
      200,
      240,
      280,
      350,
      450,
      1000
    ),
    elePtBinning2D = cms.vdouble(
      0,
      40,
      80,
      100,
      120,
      140,
      160,
      180,
      200,
      240,
      280,
      350,
      450,
      1000
    ),
    muPtBinning2D = cms.vdouble(
      0,
      40,
      80,
      100,
      120,
      140,
      160,
      180,
      200,
      240,
      280,
      350,
      450,
      1000
    ),
    jetEtaBinning2D = cms.vdouble(
      -3,
      -2,
      -1,
      0,
      1,
      2,
      3
    ),
    eleEtaBinning2D = cms.vdouble(
      -3,
      -2,
      -1,
      0,
      1,
      2,
      3
    ),
    muEtaBinning2D = cms.vdouble(
      -3,
      -2,
      -1,
      0,
      1,
      2,
      3
    ),
    phiBinning2D = cms.vdouble(
      -3.1415,
      -2.5132,
      -1.8849,
      -1.2566,
      -0.6283,
      0,
      0.6283,
      1.2566,
      1.8849,
      2.5132,
      3.1415
    ),
    lsPSet = cms.PSet(
      nbins = cms.uint32(2500)
    )
  ),
  leptonPVcuts = cms.PSet(
    dxy = cms.double(9999),
    dz = cms.double(9999)
  )
)
