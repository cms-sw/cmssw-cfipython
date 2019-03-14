import FWCore.ParameterSet.Config as cms

L1TGlobalProducer = cms.EDProducer('L1TGlobalProducer',
  MuonInputTag = cms.InputTag(''),
  EGammaInputTag = cms.InputTag(''),
  TauInputTag = cms.InputTag(''),
  JetInputTag = cms.InputTag(''),
  EtSumInputTag = cms.InputTag(''),
  ExtInputTag = cms.InputTag(''),
  AlgorithmTriggersUnprescaled = cms.bool(False),
  AlgorithmTriggersUnmasked = cms.bool(False),
  ProduceL1GtDaqRecord = cms.bool(True),
  ProduceL1GtObjectMapRecord = cms.bool(True),
  EmulateBxInEvent = cms.int32(1),
  L1DataBxInEvent = cms.int32(5),
  AlternativeNrBxBoardDaq = cms.uint32(0),
  BstLengthBytes = cms.int32(-1),
  PrescaleSet = cms.uint32(1),
  Verbosity = cms.untracked.int32(0),
  PrintL1Menu = cms.untracked.bool(False),
  TriggerMenuLuminosity = cms.string('startup'),
  PrescaleCSVFile = cms.string('prescale_L1TGlobal.csv')
)
