import FWCore.ParameterSet.Config as cms

def EmDQM(*args, **kwargs):
  mod = cms.EDProducer('EmDQM',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
