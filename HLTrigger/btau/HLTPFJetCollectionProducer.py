import FWCore.ParameterSet.Config as cms

def HLTPFJetCollectionProducer(*args, **kwargs):
  mod = cms.EDProducer('HLTPFJetCollectionProducer',
    HLTObject = cms.InputTag('TriggerFilterObjectWithRefs'),
    TriggerTypes = cms.vint32(),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
