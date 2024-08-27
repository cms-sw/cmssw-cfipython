import FWCore.ParameterSet.Config as cms

def DiJetMonitor(**kwargs):
  mod = cms.EDProducer('DiJetMonitor',
    FolderName = cms.string('HLT/JME/Jets/AK4/PF'),
    requireValidHLTPaths = cms.bool(True),
    met = cms.InputTag('pfMet'),
    dijetSrc = cms.InputTag('ak4PFJets'),
    electrons = cms.InputTag('gedGsfElectrons'),
    muons = cms.InputTag('muons'),
    njets = cms.int32(0),
    nelectrons = cms.int32(0),
    ptcut = cms.double(20),
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
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
