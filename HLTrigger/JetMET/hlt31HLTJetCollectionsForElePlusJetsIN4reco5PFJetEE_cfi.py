import FWCore.ParameterSet.Config as cms

hlt31HLTJetCollectionsForElePlusJetsIN4reco5PFJetEE = cms.EDProducer('HLTPFJetCollectionsForElePlusJets',
  HltElectronTag = cms.InputTag('triggerFilterObjectWithRefs'),
  SourceJetTag = cms.InputTag('jetCollection'),
  minDeltaR = cms.double(0.5)
)
