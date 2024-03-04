import FWCore.ParameterSet.Config as cms

def RawPCCProducer(**kwargs):
  mod = cms.EDProducer('RawPCCProducer',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
