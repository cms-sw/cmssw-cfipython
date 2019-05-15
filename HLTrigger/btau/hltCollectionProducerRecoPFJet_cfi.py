import FWCore.ParameterSet.Config as cms

hltCollectionProducerRecoPFJet = cms.EDProducer('HLTPFJetCollectionProducer',
  HLTObject = cms.InputTag('TriggerFilterObjectWithRefs'),
  TriggerTypes = cms.vint32()
)
