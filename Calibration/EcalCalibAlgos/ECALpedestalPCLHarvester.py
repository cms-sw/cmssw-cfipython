import FWCore.ParameterSet.Config as cms

def ECALpedestalPCLHarvester(*args, **kwargs):
  mod = cms.EDProducer('ECALpedestalPCLHarvester',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
