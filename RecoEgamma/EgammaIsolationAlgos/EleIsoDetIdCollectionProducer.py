import FWCore.ParameterSet.Config as cms

def EleIsoDetIdCollectionProducer(**kwargs):
  mod = cms.EDProducer('EleIsoDetIdCollectionProducer',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
