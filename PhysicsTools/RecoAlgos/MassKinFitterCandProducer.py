import FWCore.ParameterSet.Config as cms

def MassKinFitterCandProducer(*args, **kwargs):
  mod = cms.EDProducer('MassKinFitterCandProducer',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
