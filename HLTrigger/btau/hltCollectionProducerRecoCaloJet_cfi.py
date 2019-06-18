import FWCore.ParameterSet.Config as cms

hltCollectionProducerRecoCaloJet = cms.EDProducer('HLTCaloJetCollectionProducer',
  HLTObject = cms.InputTag('TriggerFilterObjectWithRefs'),
  TriggerTypes = cms.vint32(),
  mightGet = cms.optional.untracked.vstring
)
