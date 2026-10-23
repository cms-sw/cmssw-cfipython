import FWCore.ParameterSet.Config as cms

def DiDispStaMuonMonitor(*args, **kwargs):
  mod = cms.EDProducer('DiDispStaMuonMonitor',
    FolderName = cms.string('HLT/EXO/DiDispStaMuon'),
    requireValidHLTPaths = cms.bool(True),
    muons = cms.InputTag('displacedStandAloneMuons'),
    nmuons = cms.uint32(2),
    muonSelection = cms.PSet(
      general = cms.string('pt > 0'),
      pt = cms.string(''),
      dxy = cms.string('pt > 0')
    ),
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
      muonDxyPSet = cms.PSet(
        nbins = cms.required.uint32,
        xmin = cms.required.double,
        xmax = cms.required.double
      ),
      lsPSet = cms.PSet(
        nbins = cms.required.uint32,
        xmin = cms.required.double,
        xmax = cms.required.double
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
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
