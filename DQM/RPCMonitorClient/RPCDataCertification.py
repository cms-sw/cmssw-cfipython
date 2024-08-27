import FWCore.ParameterSet.Config as cms

def RPCDataCertification(**kwargs):
  mod = cms.EDProducer('RPCDataCertification',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
