import FWCore.ParameterSet.Config as cms

def ObjMonitor(**kwargs):
  mod = cms.EDProducer('ObjMonitor',
    FolderName = cms.string('HLT/OBJ'),
    requireValidHLTPaths = cms.bool(True),
    met = cms.InputTag('pfMet'),
    jets = cms.InputTag('ak4PFJetsCHS'),
    electrons = cms.InputTag('gedGsfElectrons'),
    muons = cms.InputTag('muons'),
    photons = cms.InputTag('gedPhotons'),
    tracks = cms.InputTag('generalTracks'),
    metSelection = cms.string('pt > 0'),
    jetSelection = cms.string('pt > 0'),
    jetId = cms.string(''),
    htjetSelection = cms.string('pt > 30'),
    eleSelection = cms.string('pt > 0'),
    muoSelection = cms.string('pt > 0'),
    phoSelection = cms.string('pt > 0'),
    trkSelection = cms.string('pt > 0'),
    njets = cms.int32(0),
    nelectrons = cms.int32(0),
    nmuons = cms.int32(0),
    nphotons = cms.int32(0),
    nmesons = cms.int32(0),
    numGenericTriggerEventPSet = cms.PSet(
      ReadPrescalesFromFile = cms.bool(False),
      andOr = cms.bool(False),
      andOrDcs = cms.bool(False),
      andOrHlt = cms.bool(False),
      andOrL1 = cms.bool(False),
      errorReplyDcs = cms.bool(False),
      errorReplyHlt = cms.bool(False),
      errorReplyL1 = cms.bool(False),
      l1BeforeMask = cms.bool(False),
      stage2 = cms.bool(False),
      dcsInputTag = cms.InputTag('scalersRawToDigi'),
      dcsRecordInputTag = cms.InputTag('onlineMetaDataDigis'),
      hltInputTag = cms.InputTag('TriggerResults', '', 'HLT'),
      l1tAlgBlkInputTag = cms.InputTag('gtStage2Digis'),
      l1tExtBlkInputTag = cms.InputTag('gtStage2Digis'),
      dbLabel = cms.string(''),
      hltDBKey = cms.string(''),
      dcsPartitions = cms.vint32(),
      hltPaths = cms.vstring(),
      l1Algorithms = cms.vstring(),
      verbosityLevel = cms.uint32(0)
    ),
    denGenericTriggerEventPSet = cms.PSet(
      ReadPrescalesFromFile = cms.bool(False),
      andOr = cms.bool(False),
      andOrDcs = cms.bool(False),
      andOrHlt = cms.bool(False),
      andOrL1 = cms.bool(False),
      errorReplyDcs = cms.bool(False),
      errorReplyHlt = cms.bool(False),
      errorReplyL1 = cms.bool(False),
      l1BeforeMask = cms.bool(False),
      stage2 = cms.bool(False),
      dcsInputTag = cms.InputTag('scalersRawToDigi'),
      dcsRecordInputTag = cms.InputTag('onlineMetaDataDigis'),
      hltInputTag = cms.InputTag('TriggerResults', '', 'HLT'),
      l1tAlgBlkInputTag = cms.InputTag('gtStage2Digis'),
      l1tExtBlkInputTag = cms.InputTag('gtStage2Digis'),
      dbLabel = cms.string(''),
      hltDBKey = cms.string(''),
      dcsPartitions = cms.vint32(),
      hltPaths = cms.vstring(),
      l1Algorithms = cms.vstring(),
      verbosityLevel = cms.uint32(0)
    ),
    doMETHistos = cms.bool(True),
    doJetHistos = cms.bool(True),
    doHTHistos = cms.bool(True),
    doHMesonGammaHistos = cms.bool(True),
    histoPSet = cms.PSet(
      metPSet = cms.PSet(
        nbins = cms.required.uint32,
        xmin = cms.required.double,
        xmax = cms.required.double
      ),
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
      phiPSet = cms.PSet(
        nbins = cms.required.uint32,
        xmin = cms.required.double,
        xmax = cms.required.double
      ),
      lsPSet = cms.PSet(
        nbins = cms.uint32(2500),
        xmin = cms.double(0),
        xmax = cms.double(2500)
      ),
      jetetaPSet = cms.PSet(
        nbins = cms.required.uint32,
        xmin = cms.required.double,
        xmax = cms.required.double
      ),
      detajjPSet = cms.PSet(
        nbins = cms.required.uint32,
        xmin = cms.required.double,
        xmax = cms.required.double
      ),
      dphijjPSet = cms.PSet(
        nbins = cms.required.uint32,
        xmin = cms.required.double,
        xmax = cms.required.double
      ),
      mindphijmetPSet = cms.PSet(
        nbins = cms.required.uint32,
        xmin = cms.required.double,
        xmax = cms.required.double
      ),
      jetptBinning = cms.vdouble(
        0,
        20,
        40,
        60,
        80,
        100,
        120,
        140,
        160,
        180,
        200,
        220,
        240,
        260,
        280,
        300,
        350,
        400,
        450,
        500,
        750,
        1000,
        1500
      ),
      jet1ptBinning = cms.vdouble(
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
        180,
        210,
        240,
        270,
        300,
        330,
        360,
        400,
        450,
        500,
        750,
        1000,
        1500
      ),
      jet2ptBinning = cms.vdouble(
        0,
        20,
        40,
        45,
        50,
        55,
        60,
        65,
        70,
        80,
        90,
        100,
        110,
        120,
        150,
        180,
        210,
        240,
        270,
        300,
        350,
        400,
        1000
      ),
      mjjBinning = cms.vdouble(
        0,
        200,
        400,
        600,
        620,
        640,
        660,
        680,
        700,
        720,
        740,
        760,
        780,
        800,
        850,
        900,
        950,
        1000,
        1200,
        1400,
        1600,
        1800,
        2000,
        2500,
        3000,
        4000,
        6000
      ),
      jetlsPSet = cms.PSet(
        nbins = cms.uint32(2500),
        xmin = cms.double(0),
        xmax = cms.double(2500)
      ),
      htPSet = cms.PSet(
        nbins = cms.required.uint32,
        xmin = cms.required.double,
        xmax = cms.required.double
      ),
      htBinning = cms.vdouble(
        0,
        50,
        100,
        150,
        200,
        250,
        300,
        350,
        400,
        450,
        500,
        550,
        600,
        650,
        700,
        750,
        800,
        900,
        1000,
        1200,
        1500,
        2000
      ),
      metBinning2 = cms.vdouble(
        0,
        20,
        40,
        60,
        80,
        100,
        120,
        140,
        160,
        180,
        200,
        220,
        240,
        260,
        280,
        300,
        320,
        340,
        360,
        380,
        400,
        450,
        500,
        1000
      ),
      htlsPSet = cms.PSet(
        nbins = cms.uint32(2500),
        xmin = cms.double(0),
        xmax = cms.double(2500)
      ),
      hmgetaPSet = cms.PSet(
        nbins = cms.required.uint32,
        xmin = cms.required.double,
        xmax = cms.required.double
      ),
      gammaptBinning = cms.vdouble(
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
        180,
        210,
        240,
        270,
        300,
        330,
        360,
        400,
        450,
        500,
        750,
        1000,
        1500
      ),
      mesonptBinning = cms.vdouble(
        0,
        20,
        40,
        45,
        50,
        55,
        60,
        65,
        70,
        80,
        90,
        100,
        110,
        120,
        150,
        180,
        210,
        240,
        270,
        300,
        350,
        400,
        1000
      ),
      hmglsPSet = cms.PSet(
        nbins = cms.uint32(2500),
        xmin = cms.double(0),
        xmax = cms.double(2500)
      )
    ),
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
