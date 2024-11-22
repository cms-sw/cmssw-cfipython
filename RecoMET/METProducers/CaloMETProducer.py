import FWCore.ParameterSet.Config as cms

def CaloMETProducer(*args, **kwargs):
  mod = cms.EDProducer('CaloMETProducer',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
