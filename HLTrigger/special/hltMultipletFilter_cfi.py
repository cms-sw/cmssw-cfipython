import FWCore.ParameterSet.Config as cms

hltMultipletFilter = cms.EDFilter('HLTMultipletFilter',
  saveTags = cms.bool(True),
  L1EGammaInputTag = cms.InputTag(''),
  L1EtSumInputTag = cms.InputTag(''),
  L1JetInputTag = cms.InputTag('hltCaloStage2Digis', 'Jet'),
  L1MuonInputTag = cms.InputTag(''),
  L1TauInputTag = cms.InputTag('hltCaloStage2Digis', 'Tau'),
  MinN = cms.int32(1),
  IBxMin = cms.int32(0),
  IBxMax = cms.int32(0),
  MinEta = cms.double(1.305),
  MaxEta = cms.double(3),
  MinPhi = cms.double(5.4105),
  MaxPhi = cms.double(5.5796),
  MinPt = cms.double(20)
)
