import FWCore.ParameterSet.Config as cms

def ManyIntWhenRegisteredProducer(*args, **kwargs):
  mod = cms.EDProducer('ManyIntWhenRegisteredProducer',
    src = cms.required.string,
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
