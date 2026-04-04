import FWCore.ParameterSet.Config as cms

def ProdigalProducer(*args, **kwargs):
  mod = cms.EDProducer('ProdigalProducer',
    label = cms.required.string,
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
