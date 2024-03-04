import FWCore.ParameterSet.Config as cms

def ECALpedestalPCLworker(**kwargs):
  mod = cms.EDProducer('ECALpedestalPCLworker',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
