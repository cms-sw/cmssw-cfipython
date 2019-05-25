import FWCore.ParameterSet.Config as cms

hltMETCleanerUsingJetID = cms.EDProducer('HLTMETCleanerUsingJetID',
  minPt = cms.double(20),
  maxEta = cms.double(5),
  metLabel = cms.InputTag('hltMet'),
  jetsLabel = cms.InputTag('hltAntiKT4CaloJets'),
  goodJetsLabel = cms.InputTag('hltCaloJetIDPassed')
)
