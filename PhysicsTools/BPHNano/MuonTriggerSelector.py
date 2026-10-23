import FWCore.ParameterSet.Config as cms

def MuonTriggerSelector(*args, **kwargs):
  mod = cms.EDProducer('MuonTriggerSelector',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
