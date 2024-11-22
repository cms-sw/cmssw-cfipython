import FWCore.ParameterSet.Config as cms

def ElseMETProducer(*args, **kwargs):
  mod = cms.EDProducer('ElseMETProducer',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
