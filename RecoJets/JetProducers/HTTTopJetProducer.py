import FWCore.ParameterSet.Config as cms

def HTTTopJetProducer(*args, **kwargs):
  mod = cms.EDProducer('HTTTopJetProducer',
    optimalR = cms.bool(True),
    qJets = cms.bool(False),
    minFatjetPt = cms.double(200),
    minSubjetPt = cms.double(0),
    minCandPt = cms.double(0),
    maxFatjetAbsEta = cms.double(99),
    subjetMass = cms.double(30),
    filtR = cms.double(0.3),
    filtN = cms.int32(5),
    mode = cms.int32(4),
    minCandMass = cms.double(0),
    maxCandMass = cms.double(999999),
    massRatioWidth = cms.double(999999),
    minM23Cut = cms.double(0),
    minM13Cut = cms.double(0),
    maxM13Cut = cms.double(999999),
    maxR = cms.double(1.5),
    minR = cms.double(0.5),
    rejectMinR = cms.bool(False),
    verbose = cms.bool(False),
    algorithm = cms.int32(1),
    useMassDropTagger = cms.bool(False),
    useFiltering = cms.bool(False),
    useDynamicFiltering = cms.bool(False),
    useTrimming = cms.bool(False),
    usePruning = cms.bool(False),
    useCMSBoostedTauSeedingAlgorithm = cms.bool(False),
    useKtPruning = cms.bool(False),
    useConstituentSubtraction = cms.bool(False),
    useSoftDrop = cms.bool(False),
    correctShape = cms.bool(False),
    UseOnlyVertexTracks = cms.bool(False),
    UseOnlyOnePV = cms.bool(False),
    muCut = cms.double(-1),
    yCut = cms.double(-1),
    rFilt = cms.double(-1),
    rFiltFactor = cms.double(-1),
    trimPtFracMin = cms.double(-1),
    zcut = cms.double(-1),
    rcut_factor = cms.double(-1),
    csRho_EtaMax = cms.double(-1),
    csRParam = cms.double(-1),
    beta = cms.double(-1),
    R0 = cms.double(-1),
    gridMaxRapidity = cms.double(-1),
    gridSpacing = cms.double(-1),
    DzTrVtxMax = cms.double(999999),
    DxyTrVtxMax = cms.double(999999),
    MaxVtxZ = cms.double(15),
    subjetPtMin = cms.double(-1),
    muMin = cms.double(-1),
    muMax = cms.double(-1),
    yMin = cms.double(-1),
    yMax = cms.double(-1),
    dRMin = cms.double(-1),
    dRMax = cms.double(-1),
    maxDepth = cms.int32(-1),
    nFilt = cms.int32(-1),
    MinVtxNdof = cms.int32(5),
    jetCollInstanceName = cms.string('SubJets'),
    src = cms.InputTag('particleFlow'),
    srcPVs = cms.InputTag(''),
    jetType = cms.string('PFJet'),
    jetAlgorithm = cms.string('AntiKt'),
    rParam = cms.double(0.4),
    inputEtMin = cms.double(0),
    inputEMin = cms.double(0),
    jetPtMin = cms.double(5),
    doPVCorrection = cms.bool(False),
    doAreaFastjet = cms.bool(False),
    doRhoFastjet = cms.bool(False),
    doPUOffsetCorr = cms.bool(False),
    puPtMin = cms.double(10),
    nSigmaPU = cms.double(1),
    radiusPU = cms.double(0.5),
    subtractorName = cms.string(''),
    useExplicitGhosts = cms.bool(False),
    doAreaDiskApprox = cms.bool(False),
    voronoiRfact = cms.double(-0.9),
    Rho_EtaMax = cms.double(4.4),
    Ghost_EtaMax = cms.double(5),
    Active_Area_Repeats = cms.int32(1),
    GhostArea = cms.double(0.01),
    restrictInputs = cms.bool(False),
    maxInputs = cms.uint32(1),
    writeCompound = cms.bool(False),
    writeJetsWithConst = cms.bool(False),
    doFastJetNonUniform = cms.bool(False),
    useDeterministicSeed = cms.bool(False),
    minSeed = cms.uint32(14327),
    verbosity = cms.int32(0),
    puWidth = cms.double(0),
    nExclude = cms.uint32(0),
    maxBadEcalCells = cms.uint32(9999999),
    maxBadHcalCells = cms.uint32(9999999),
    maxProblematicEcalCells = cms.uint32(9999999),
    maxProblematicHcalCells = cms.uint32(9999999),
    maxRecoveredEcalCells = cms.uint32(9999999),
    maxRecoveredHcalCells = cms.uint32(9999999),
    puCenters = cms.vdouble(),
    applyWeight = cms.bool(False),
    srcWeights = cms.InputTag(''),
    minimumTowersFraction = cms.double(0),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
