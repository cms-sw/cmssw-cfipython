import FWCore.ParameterSet.Config as cms

hlt21HLTCollectionProducerIN4reco5PFJetEE = cms.EDProducer('HLTPFJetCollectionProducer',
  HLTObject = cms.InputTag('TriggerFilterObjectWithRefs'),
  TriggerTypes = cms.vint32()
)
