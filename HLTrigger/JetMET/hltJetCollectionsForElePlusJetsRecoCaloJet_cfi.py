import FWCore.ParameterSet.Config as cms

hltJetCollectionsForElePlusJetsRecoCaloJet = cms.EDProducer('HLTCaloJetCollectionsForElePlusJets',
  HltElectronTag = cms.InputTag('triggerFilterObjectWithRefs'),
  SourceJetTag = cms.InputTag('jetCollection'),
  minDeltaR = cms.double(0.5)
)
