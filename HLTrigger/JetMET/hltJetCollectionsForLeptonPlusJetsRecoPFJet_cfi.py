import FWCore.ParameterSet.Config as cms

hltJetCollectionsForLeptonPlusJetsRecoPFJet = cms.EDProducer('HLTPFJetCollectionsForLeptonPlusJets',
  HltLeptonTag = cms.InputTag('triggerFilterObjectWithRefs'),
  SourceJetTag = cms.InputTag('caloJetCollection'),
  minDeltaR = cms.double(0.5)
)
