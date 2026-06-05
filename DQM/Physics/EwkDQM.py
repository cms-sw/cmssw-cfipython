import FWCore.ParameterSet.Config as cms

def EwkDQM(*args, **kwargs):
  mod = cms.EDProducer('EwkDQM',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
