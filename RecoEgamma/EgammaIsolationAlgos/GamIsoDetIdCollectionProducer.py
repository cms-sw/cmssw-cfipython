import FWCore.ParameterSet.Config as cms

def GamIsoDetIdCollectionProducer(*args, **kwargs):
  mod = cms.EDProducer('GamIsoDetIdCollectionProducer',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
