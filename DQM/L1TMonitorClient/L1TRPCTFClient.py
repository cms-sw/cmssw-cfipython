import FWCore.ParameterSet.Config as cms

def L1TRPCTFClient(**kwargs):
  mod = cms.EDProducer('L1TRPCTFClient',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
