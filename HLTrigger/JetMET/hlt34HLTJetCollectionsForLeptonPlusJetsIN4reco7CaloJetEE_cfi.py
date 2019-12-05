import FWCore.ParameterSet.Config as cms

hlt34HLTJetCollectionsForLeptonPlusJetsIN4reco7CaloJetEE = cms.EDProducer('HLTCaloJetCollectionsForLeptonPlusJets',
  HltLeptonTag = cms.InputTag('triggerFilterObjectWithRefs'),
  SourceJetTag = cms.InputTag('caloJetCollection'),
  minDeltaR = cms.double(0.5)
)
