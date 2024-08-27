import FWCore.ParameterSet.Config as cms

def RawDataCollectorByLabel(**kwargs):
  mod = cms.EDProducer('RawDataCollectorByLabel',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
