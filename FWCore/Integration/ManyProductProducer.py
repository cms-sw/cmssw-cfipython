import FWCore.ParameterSet.Config as cms

def ManyProductProducer(*args, **kwargs):
  mod = cms.EDProducer('ManyProductProducer',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
