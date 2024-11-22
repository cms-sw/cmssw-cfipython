import FWCore.ParameterSet.Config as cms

def EgHLTOfflineSource(*args, **kwargs):
  mod = cms.EDProducer('EgHLTOfflineSource',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
