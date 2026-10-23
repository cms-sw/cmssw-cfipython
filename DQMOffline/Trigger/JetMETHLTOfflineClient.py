import FWCore.ParameterSet.Config as cms

def JetMETHLTOfflineClient(*args, **kwargs):
  mod = cms.EDProducer('JetMETHLTOfflineClient',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
