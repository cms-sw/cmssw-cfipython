import FWCore.ParameterSet.Config as cms

hltJetL1TMatchProducerRecoCaloJet = cms.EDProducer('HLTCaloJetL1TMatchProducer',
  jetsInput = cms.InputTag('hltAntiKT5PFJets'),
  L1Jets = cms.InputTag('hltCaloStage2Digis'),
  DeltaR = cms.double(0.5)
)
