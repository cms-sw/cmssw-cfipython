import FWCore.ParameterSet.Config as cms

def LepHTMonitor(*args, **kwargs):
  mod = cms.EDProducer('LepHTMonitor',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
