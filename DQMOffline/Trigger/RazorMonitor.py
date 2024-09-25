import FWCore.ParameterSet.Config as cms

def RazorMonitor(*args, **kwargs):
  mod = cms.EDProducer('RazorMonitor',
    FolderName = cms.string('HLT/SUSY/Razor'),
    requireValidHLTPaths = cms.bool(True),
    met = cms.InputTag('pfMet'),
    jets = cms.InputTag('ak4PFJetsCHS'),
    hemispheres = cms.InputTag('hemispheresDQM'),
    metSelection = cms.string('pt > 0'),
    jetSelection = cms.string('pt > 80'),
    njets = cms.uint32(2),
    mrCut = cms.double(300),
    rsqCut = cms.double(0.15),
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
    ),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
