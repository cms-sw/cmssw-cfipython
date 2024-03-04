import FWCore.ParameterSet.Config as cms

def JetMETHLTOfflineClient(**kwargs):
  mod = cms.EDProducer('JetMETHLTOfflineClient',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
