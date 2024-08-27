import FWCore.ParameterSet.Config as cms

def HLTObjectMonitor(**kwargs):
  mod = cms.EDProducer('HLTObjectMonitor',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
