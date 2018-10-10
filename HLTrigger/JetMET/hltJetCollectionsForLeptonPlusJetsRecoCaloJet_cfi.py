import FWCore.ParameterSet.Config as cms

hltJetCollectionsForLeptonPlusJetsRecoCaloJet = cms.EDProducer('HLTCaloJetCollectionsForLeptonPlusJets',
  HltLeptonTag = cms.InputTag('triggerFilterObjectWithRefs'),
  SourceJetTag = cms.InputTag('caloJetCollection'),
  minDeltaR = cms.double(0.5)
)
