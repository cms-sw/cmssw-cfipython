import FWCore.ParameterSet.Config as cms

def EgHLTOfflineClient(*args, **kwargs):
  mod = cms.EDProducer('EgHLTOfflineClient',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
