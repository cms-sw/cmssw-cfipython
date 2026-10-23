import FWCore.ParameterSet.Config as cms

def DeepCMVATagInfoProducer(*args, **kwargs):
  mod = cms.EDProducer('DeepCMVATagInfoProducer',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
