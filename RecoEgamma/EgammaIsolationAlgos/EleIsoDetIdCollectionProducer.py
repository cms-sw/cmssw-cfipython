import FWCore.ParameterSet.Config as cms

def EleIsoDetIdCollectionProducer(*args, **kwargs):
  mod = cms.EDProducer('EleIsoDetIdCollectionProducer',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
