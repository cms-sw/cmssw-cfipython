import FWCore.ParameterSet.Config as cms

hlt21HLTCollectionProducerIN4reco7CaloJetEE = cms.EDProducer('HLTCaloJetCollectionProducer',
  HLTObject = cms.InputTag('TriggerFilterObjectWithRefs'),
  TriggerTypes = cms.vint32()
)
