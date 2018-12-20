import FWCore.ParameterSet.Config as cms

hltJetCollectionsForElePlusJetsRecoPFJet = cms.EDProducer('HLTPFJetCollectionsForElePlusJets',
  HltElectronTag = cms.InputTag('triggerFilterObjectWithRefs'),
  SourceJetTag = cms.InputTag('jetCollection'),
  minDeltaR = cms.double(0.5)
)
