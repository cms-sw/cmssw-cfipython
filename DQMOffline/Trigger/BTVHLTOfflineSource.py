import FWCore.ParameterSet.Config as cms

def BTVHLTOfflineSource(*args, **kwargs):
  mod = cms.EDProducer('BTVHLTOfflineSource',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
