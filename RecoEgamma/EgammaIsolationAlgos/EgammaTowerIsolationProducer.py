import FWCore.ParameterSet.Config as cms

def EgammaTowerIsolationProducer(*args, **kwargs):
  mod = cms.EDProducer('EgammaTowerIsolationProducer',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
