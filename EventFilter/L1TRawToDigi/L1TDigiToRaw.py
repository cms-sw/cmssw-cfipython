import FWCore.ParameterSet.Config as cms

def L1TDigiToRaw(*args, **kwargs):
  mod = cms.EDProducer('L1TDigiToRaw',
    FWId = cms.uint32(4294967295),
    FedId = cms.required.int32,
    eventType = cms.untracked.int32(1),
    Setup = cms.required.string,
    InputLabel = cms.InputTag(''),
    InputLabel2 = cms.InputTag(''),
    lenSlinkHeader = cms.untracked.int32(8),
    lenSlinkTrailer = cms.untracked.int32(8),
    CTP7 = cms.untracked.bool(False),
    TauInputLabel = cms.optional.InputTag,
    IsoTauInputLabel = cms.optional.InputTag,
    HFBitCountsInputLabel = cms.optional.InputTag,
    HFRingSumsInputLabel = cms.optional.InputTag,
    RegionInputLabel = cms.optional.InputTag,
    EmCandInputLabel = cms.optional.InputTag,
    EMTFInputLabelAWB = cms.optional.InputTag,
    ecalDigis = cms.optional.InputTag,
    hcalDigis = cms.optional.InputTag,
    caloRegions = cms.optional.InputTag,
    TowerInputLabel = cms.optional.InputTag,
    GtInputTag = cms.optional.InputTag,
    ExtInputTag = cms.optional.InputTag,
    MuonInputTag = cms.optional.InputTag,
    ShowerInputTag = cms.optional.InputTag,
    EGammaInputTag = cms.optional.InputTag,
    JetInputTag = cms.optional.InputTag,
    TauInputTag = cms.optional.InputTag,
    EtSumInputTag = cms.optional.InputTag,
    EtSumZDCInputTag = cms.optional.InputTag,
    BMTFInputLabel = cms.optional.InputTag,
    OMTFInputLabel = cms.optional.InputTag,
    EMTFInputLabel = cms.optional.InputTag,
    ImdInputLabelBMTF = cms.optional.InputTag,
    ImdInputLabelEMTFNeg = cms.optional.InputTag,
    ImdInputLabelEMTFPos = cms.optional.InputTag,
    ImdInputLabelOMTFNeg = cms.optional.InputTag,
    ImdInputLabelOMTFPos = cms.optional.InputTag,
    ShowerInputLabel = cms.optional.InputTag,
    EMTFShowerInputLabel = cms.optional.InputTag,
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
