import FWCore.ParameterSet.Config as cms

def LepHTMonitor(**kwargs):
  mod = cms.EDProducer('LepHTMonitor',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
