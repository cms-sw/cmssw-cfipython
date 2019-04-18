import FWCore.ParameterSet.Config as cms

hltJetCollectionsForBoostedLeptonPlusJetsRecoPFJet = cms.EDProducer('HLTPFJetCollectionsForBoostedLeptonPlusJets',
  HltLeptonTag = cms.InputTag('triggerFilterObjectWithRefs'),
  SourceJetTag = cms.InputTag('jetCollection'),
  minDeltaR = cms.double(0.5)
)
