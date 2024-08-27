import FWCore.ParameterSet.Config as cms

def L1TDTTFClient(**kwargs):
  mod = cms.EDProducer('L1TDTTFClient',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
