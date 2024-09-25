import FWCore.ParameterSet.Config as cms

def JetMETHLTOfflineSource(*args, **kwargs):
  mod = cms.EDProducer('JetMETHLTOfflineSource',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
