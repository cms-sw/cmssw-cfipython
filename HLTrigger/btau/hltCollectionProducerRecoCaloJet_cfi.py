import FWCore.ParameterSet.Config as cms

hltCollectionProducerRecoCaloJet = cms.EDProducer('HLTCaloJetCollectionProducer',
  HLTObject = cms.InputTag('TriggerFilterObjectWithRefs'),
  TriggerTypes = cms.vint32()
)
