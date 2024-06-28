import FWCore.ParameterSet.Config as cms

def L1TGlobalProducer(**kwargs):
  mod = cms.EDProducer('L1TGlobalProducer',
    MuonInputTag = cms.InputTag(''),
    MuonShowerInputTag = cms.InputTag(''),
    EGammaInputTag = cms.InputTag(''),
    TauInputTag = cms.InputTag(''),
    JetInputTag = cms.InputTag(''),
    EtSumInputTag = cms.InputTag(''),
    EtSumZdcInputTag = cms.InputTag(''),
    CICADAInputTag = cms.InputTag(''),
    ExtInputTag = cms.InputTag(''),
    AlgoBlkInputTag = cms.InputTag('hltGtStage2Digis'),
    GetPrescaleColumnFromData = cms.bool(False),
    AlgorithmTriggersUnprescaled = cms.bool(False),
    RequireMenuToMatchAlgoBlkInput = cms.bool(True),
    AlgorithmTriggersUnmasked = cms.bool(False),
    useMuonShowers = cms.bool(False),
    resetPSCountersEachLumiSec = cms.bool(False),
    semiRandomInitialPSCounters = cms.bool(False),
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
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
