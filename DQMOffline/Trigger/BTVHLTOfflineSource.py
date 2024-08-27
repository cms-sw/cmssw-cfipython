import FWCore.ParameterSet.Config as cms

def BTVHLTOfflineSource(**kwargs):
  mod = cms.EDProducer('BTVHLTOfflineSource',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
