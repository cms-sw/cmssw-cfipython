import FWCore.ParameterSet.Config as cms

def HLTCaloJetCollectionProducer(**kwargs):
  mod = cms.EDProducer('HLTCaloJetCollectionProducer',
    HLTObject = cms.InputTag('TriggerFilterObjectWithRefs'),
    TriggerTypes = cms.vint32(),
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
