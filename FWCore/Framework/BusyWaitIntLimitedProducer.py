import FWCore.ParameterSet.Config as cms

def BusyWaitIntLimitedProducer(*args, **kwargs):
  mod = cms.EDProducer('BusyWaitIntLimitedProducer',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
