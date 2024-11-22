import FWCore.ParameterSet.Config as cms

def RawDataSelector(*args, **kwargs):
  mod = cms.EDProducer('RawDataSelector',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
