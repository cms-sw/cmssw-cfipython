import FWCore.ParameterSet.Config as cms

razorMonitoring = cms.EDAnalyzer('RazorMonitor',
  FolderName = cms.string('HLT/SUSY/Razor'),
  met = cms.InputTag('pfMet'),
  jets = cms.InputTag('ak4PFJetsCHS'),
  hemispheres = cms.InputTag('hemispheresDQM'),
  metSelection = cms.string('pt > 0'),
  jetSelection = cms.string('pt > 80'),
  njets = cms.uint32(2),
  mrCut = cms.double(300),
  rsqCut = cms.double(0.15),
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
    mrBins = cms.vdouble(
      0,
      100,
      200,
      300,
      400,
      500,
      575,
      650,
      750,
      900,
      1200,
      1600,
      2500,
      4000
    ),
    rsqBins = cms.vdouble(
      0,
      0.05,
      0.1,
      0.15,
      0.2,
      0.25,
      0.3,
      0.41,
      0.52,
      0.64,
      0.8,
      1.5
    ),
    dphiRBins = cms.vdouble(
      0,
      0.5,
      1,
      1.5,
      2,
      2.5,
      2.8,
      3,
      3.2
    )
  )
)
