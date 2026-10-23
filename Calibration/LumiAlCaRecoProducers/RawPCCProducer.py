import FWCore.ParameterSet.Config as cms

def RawPCCProducer(*args, **kwargs):
  mod = cms.EDProducer('RawPCCProducer',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
