import FWCore.ParameterSet.Config as cms

def RawDataCollectorByLabel(*args, **kwargs):
  mod = cms.EDProducer('RawDataCollectorByLabel',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
