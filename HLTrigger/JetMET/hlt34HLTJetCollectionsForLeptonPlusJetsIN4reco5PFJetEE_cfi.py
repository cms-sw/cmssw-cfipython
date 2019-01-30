import FWCore.ParameterSet.Config as cms

hlt34HLTJetCollectionsForLeptonPlusJetsIN4reco5PFJetEE = cms.EDProducer('HLTPFJetCollectionsForLeptonPlusJets',
  HltLeptonTag = cms.InputTag('triggerFilterObjectWithRefs'),
  SourceJetTag = cms.InputTag('caloJetCollection'),
  minDeltaR = cms.double(0.5)
)
