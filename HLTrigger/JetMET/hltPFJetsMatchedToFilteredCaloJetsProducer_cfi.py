import FWCore.ParameterSet.Config as cms

hltPFJetsMatchedToFilteredCaloJetsProducer = cms.EDProducer('PFJetsMatchedToFilteredCaloJetsProducer',
  PFJetSrc = cms.InputTag('hltPFJets'),
  CaloJetFilter = cms.InputTag('hltSingleJet240Regional'),
  DeltaR = cms.double(0.5),
  TriggerType = cms.int32(85)
)
