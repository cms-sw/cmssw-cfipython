import FWCore.ParameterSet.Config as cms

hlt31HLTJetCollectionsForElePlusJetsIN4reco7CaloJetEE = cms.EDProducer('HLTCaloJetCollectionsForElePlusJets',
  HltElectronTag = cms.InputTag('triggerFilterObjectWithRefs'),
  SourceJetTag = cms.InputTag('jetCollection'),
  minDeltaR = cms.double(0.5)
)
