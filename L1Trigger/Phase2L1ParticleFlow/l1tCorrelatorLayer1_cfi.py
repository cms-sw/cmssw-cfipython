import FWCore.ParameterSet.Config as cms

l1tCorrelatorLayer1 = cms.EDProducer('L1TCorrelatorLayer1Producer',
  tracks = cms.InputTag(''),
  muons = cms.InputTag('l1tSAMuonsGmt', 'promptSAMuons'),
  emClusters = cms.VInputTag(),
  hadClusters = cms.VInputTag(),
  vtxCollection = cms.InputTag('l1tVertexFinderEmulator', 'L1VerticesEmulation'),
  vtxCollectionEmulation = cms.bool(True),
  emPtCut = cms.double(0),
  hadPtCut = cms.double(0),
  trkPtCut = cms.double(0),
  nVtx = cms.required.int32,
  trackInputConversionAlgo = cms.string('Ideal'),
  muonInputConversionAlgo = cms.string('Ideal'),
  hgcalInputConversionAlgo = cms.string('Ideal'),
  regionizerAlgo = cms.string('Ideal'),
  regionizerAlgoParameters = cms.PSet(
    useAlsoVtxCoords = cms.bool(True),
    debug = cms.untracked.bool(False)
  ),
  pfAlgo = cms.string('PFAlgo3'),
  pfAlgoParameters = cms.PSet(
    nTrack = cms.uint32(25),
    nCalo = cms.uint32(18),
    nMu = cms.uint32(2),
    nSelCalo = cms.uint32(18),
    nEmCalo = cms.uint32(12),
    nPhoton = cms.uint32(12),
    nAllNeutral = cms.uint32(25),
    trackMuDR = cms.double(0.2),
    trackEmDR = cms.double(0.04),
    emCaloDR = cms.double(0.1),
    trackCaloDR = cms.double(0.15),
    maxInvisiblePt = cms.double(10),
    tightTrackMaxInvisiblePt = cms.double(20),
    caloResolution = cms.PSet(
      etaBins = cms.required.vdouble,
      offset = cms.required.vdouble,
      scale = cms.required.vdouble
    ),
    debug = cms.untracked.bool(False)
  ),
  puAlgo = cms.string('LinearizedPuppi'),
  puAlgoParameters = cms.PSet(
    nTrack = cms.required.uint32,
    nIn = cms.required.uint32,
    nOut = cms.required.uint32,
    nVtx = cms.uint32(1),
    dZ = cms.required.double,
    dr = cms.required.double,
    drMin = cms.required.double,
    ptMax = cms.required.double,
    absEtaCuts = cms.required.vdouble,
    ptCut = cms.required.vdouble,
    ptSlopes = cms.required.vdouble,
    ptSlopesPhoton = cms.required.vdouble,
    ptZeros = cms.required.vdouble,
    ptZerosPhoton = cms.required.vdouble,
    alphaSlopes = cms.required.vdouble,
    alphaZeros = cms.required.vdouble,
    alphaCrop = cms.required.vdouble,
    priors = cms.required.vdouble,
    priorsPhoton = cms.required.vdouble,
    nFinalSort = cms.required.uint32,
    finalSortAlgo = cms.string('Insertion'),
    fakePuppi = cms.bool(False),
    debug = cms.untracked.bool(False)
  ),
  tkEgAlgoParameters = cms.PSet(
    nTRACK = cms.required.uint32,
    nTRACK_EGIN = cms.required.uint32,
    nEMCALO_EGIN = cms.required.uint32,
    nEM_EGOUT = cms.required.uint32,
    doBremRecovery = cms.bool(False),
    writeBeforeBremRecovery = cms.bool(False),
    filterHwQuality = cms.bool(False),
    caloHwQual = cms.int32(4),
    doEndcapHwQual = cms.bool(False),
    dEtaMaxBrem = cms.double(0.02),
    dPhiMaxBrem = cms.double(0.1),
    absEtaBoundaries = cms.vdouble(
      0,
      0.9,
      1.5
    ),
    dEtaValues = cms.vdouble(
      0.025,
      0.015,
      0.01
    ),
    dPhiValues = cms.vdouble(
      0.07,
      0.07,
      0.07
    ),
    caloEtMin = cms.double(0),
    trkQualityPtMin = cms.double(10),
    writeEGSta = cms.bool(False),
    tkIsoParametersTkEm = cms.PSet(
      tkQualityPtMin = cms.required.double,
      dZ = cms.double(0.6),
      dRMin = cms.required.double,
      dRMax = cms.required.double
    ),
    tkIsoParametersTkEle = cms.PSet(
      tkQualityPtMin = cms.required.double,
      dZ = cms.double(0.6),
      dRMin = cms.required.double,
      dRMax = cms.required.double
    ),
    pfIsoParametersTkEm = cms.PSet(
      tkQualityPtMin = cms.required.double,
      dZ = cms.double(0.6),
      dRMin = cms.required.double,
      dRMax = cms.required.double
    ),
    pfIsoParametersTkEle = cms.PSet(
      tkQualityPtMin = cms.required.double,
      dZ = cms.double(0.6),
      dRMin = cms.required.double,
      dRMax = cms.required.double
    ),
    doTkIso = cms.bool(True),
    doPfIso = cms.bool(True),
    hwIsoTypeTkEle = cms.uint32(0),
    hwIsoTypeTkEm = cms.uint32(2),
    doCompositeTkEle = cms.bool(False),
    nCompCandPerCluster = cms.uint32(3),
    compositeParametersTkEle = cms.PSet(
      loose_wp = cms.double(-0.732422),
      tight_wp = cms.double(0.214844),
      model = cms.string('L1Trigger/Phase2L1ParticleFlow/data/compositeID.json')
    )
  ),
  tkEgSorterAlgo = cms.string('Barrel'),
  tkEgSorterParameters = cms.PSet(
    nObjToSort = cms.required.uint32,
    nObjSorted = cms.required.uint32
  ),
  caloSectors = cms.required.VPSet,
  regions = cms.required.VPSet,
  boards = cms.required.VPSet,
  dumpFileName = cms.untracked.string(''),
  writeRawHgcalCluster = cms.untracked.bool(False),
  patternWriters = cms.untracked.VPSet(
  ),
  debugEta = cms.untracked.double(0),
  debugPhi = cms.untracked.double(0),
  debugR = cms.untracked.double(-1),
  mightGet = cms.optional.untracked.vstring
)
