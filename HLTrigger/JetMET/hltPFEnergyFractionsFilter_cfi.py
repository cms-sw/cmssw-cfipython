import FWCore.ParameterSet.Config as cms

hltPFEnergyFractionsFilter = cms.EDFilter('HLTPFEnergyFractionsFilter',
  saveTags = cms.bool(True),
  inputPFJetTag = cms.InputTag('hltAntiKT5PFJets'),
  nJet = cms.uint32(1),
  min_CEEF = cms.double(-99),
  max_CEEF = cms.double(99),
  min_NEEF = cms.double(-99),
  max_NEEF = cms.double(99),
  min_CHEF = cms.double(-99),
  max_CHEF = cms.double(99),
  min_NHEF = cms.double(-99),
  max_NHEF = cms.double(99),
  triggerType = cms.int32(85)
)
