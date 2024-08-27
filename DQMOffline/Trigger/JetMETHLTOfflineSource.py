import FWCore.ParameterSet.Config as cms

def JetMETHLTOfflineSource(**kwargs):
  mod = cms.EDProducer('JetMETHLTOfflineSource',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
