import FWCore.ParameterSet.Config as cms

def DSVProducer(*args, **kwargs):
  mod = cms.EDProducer('DSVProducer',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
