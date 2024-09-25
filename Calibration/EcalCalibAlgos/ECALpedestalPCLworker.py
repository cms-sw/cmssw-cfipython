import FWCore.ParameterSet.Config as cms

def ECALpedestalPCLworker(*args, **kwargs):
  mod = cms.EDProducer('ECALpedestalPCLworker',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
