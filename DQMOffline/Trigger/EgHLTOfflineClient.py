import FWCore.ParameterSet.Config as cms

def EgHLTOfflineClient(**kwargs):
  mod = cms.EDProducer('EgHLTOfflineClient',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
