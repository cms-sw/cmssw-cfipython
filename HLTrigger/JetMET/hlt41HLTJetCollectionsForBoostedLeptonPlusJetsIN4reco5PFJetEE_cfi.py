import FWCore.ParameterSet.Config as cms

hlt41HLTJetCollectionsForBoostedLeptonPlusJetsIN4reco5PFJetEE = cms.EDProducer('HLTPFJetCollectionsForBoostedLeptonPlusJets',
  HltLeptonTag = cms.InputTag('triggerFilterObjectWithRefs'),
  SourceJetTag = cms.InputTag('jetCollection'),
  minDeltaR = cms.double(0.5)
)
