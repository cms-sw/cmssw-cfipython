import FWCore.ParameterSet.Config as cms

def RawDataSelector(**kwargs):
  mod = cms.EDProducer('RawDataSelector',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
