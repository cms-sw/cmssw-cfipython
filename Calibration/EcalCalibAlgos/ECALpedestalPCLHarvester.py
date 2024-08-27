import FWCore.ParameterSet.Config as cms

def ECALpedestalPCLHarvester(**kwargs):
  mod = cms.EDProducer('ECALpedestalPCLHarvester',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
