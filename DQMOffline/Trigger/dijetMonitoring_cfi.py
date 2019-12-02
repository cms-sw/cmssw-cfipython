import FWCore.ParameterSet.Config as cms

dijetMonitoring = cms.EDProducer('DiJetMonitor',
  FolderName = cms.string('HLT/JME/Jets/AK4/PF'),
  met = cms.InputTag('pfMet'),
  dijetSrc = cms.InputTag('ak4PFJets'),
  electrons = cms.InputTag('gedGsfElectrons'),
  muons = cms.InputTag('muons'),
  njets = cms.int32(0),
  nelectrons = cms.int32(0),
  ptcut = cms.double(20),
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
    errorReplyHlt = cms.bool(False),
    verbosityLevel = cms.uint32(1)
  ),
  histoPSet = cms.PSet(
    dijetPSet = cms.PSet(
      nbins = cms.required.uint32,
      xmin = cms.required.double,
      xmax = cms.required.double
    ),
    dijetPtThrPSet = cms.PSet(
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
      nbins = cms.uint32(2500),
      xmin = cms.double(0),
      xmax = cms.double(2500)
    )
  ),
  mightGet = cms.optional.untracked.vstring
)
