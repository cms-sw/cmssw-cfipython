import FWCore.ParameterSet.Config as cms

def BTagAndProbe(**kwargs):
  mod = cms.EDProducer('BTagAndProbe',
    FolderName = cms.string('HLT/BTV'),
    requireValidHLTPaths = cms.bool(True),
    vertices = cms.InputTag('offlinePrimaryVertices'),
    muons = cms.InputTag('muons'),
    electrons = cms.InputTag('gedGsfElectrons'),
    elecID = cms.InputTag('egmGsfElectronIDsForDQM', 'cutBasedElectronID-RunIIIWinter22-V1-tight'),
    btagAlgos = cms.VInputTag(
      'pfDeepCSVJetTags:probb',
      'pfDeepCSVJetTags:probbb'
    ),
    jetSelection = cms.string('pt > 30'),
    eleSelection = cms.string('pt > 0 && abs(eta) < 2.5'),
    muoSelection = cms.string('pt > 6 && abs(eta) < 2.4'),
    vertexSelection = cms.string('!isFake'),
    bjetSelection = cms.string('pt > 30'),
    nelectrons = cms.uint32(0),
    nmuons = cms.uint32(0),
    leptJetDeltaRmin = cms.double(0),
    bJetMuDeltaRmax = cms.double(9999),
    bJetDeltaEtaMax = cms.double(9999),
    nbjets = cms.uint32(0),
    workingpoint = cms.double(0.4941),
    applyLeptonPVcuts = cms.bool(False),
    debug = cms.bool(False),
    genericTriggerEventPSet = cms.PSet(
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
    leptonPVcuts = cms.PSet(
      dxy = cms.double(9999),
      dz = cms.double(9999)
    ),
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
