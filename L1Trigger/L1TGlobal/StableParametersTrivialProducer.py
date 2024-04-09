import FWCore.ParameterSet.Config as cms

def StableParametersTrivialProducer(**kwargs):
  mod = cms.ESProducer('StableParametersTrivialProducer',
    TotalBxInEvent = cms.int32(5),
    NumberPhysTriggers = cms.uint32(512),
    NumberL1Muon = cms.uint32(12),
    NumberL1EGamma = cms.uint32(12),
    NumberL1Jet = cms.uint32(12),
    NumberL1Tau = cms.uint32(8),
    NumberChips = cms.uint32(5),
    PinsOnChip = cms.uint32(512),
    OrderOfChip = cms.vint32(1),
    NumberL1IsoEG = cms.uint32(0),
    NumberL1JetCounts = cms.uint32(0),
    UnitLength = cms.int32(0),
    NumberL1ForJet = cms.uint32(0),
    IfCaloEtaNumberBits = cms.uint32(0),
    IfMuEtaNumberBits = cms.uint32(0),
    NumberL1TauJet = cms.uint32(0),
    NumberL1Mu = cms.uint32(0),
    NumberConditionChips = cms.uint32(0),
    NumberPsbBoards = cms.int32(0),
    NumberL1CenJet = cms.uint32(0),
    PinsOnConditionChip = cms.uint32(0),
    NumberL1NoIsoEG = cms.uint32(0),
    NumberTechnicalTriggers = cms.uint32(0),
    NumberPhysTriggersExtended = cms.uint32(0),
    WordLength = cms.int32(0),
    OrderConditionChip = cms.vint32(1),
    appendToDataLabel = cms.string('')
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod