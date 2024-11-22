import FWCore.ParameterSet.Config as cms

def EwkElecDQM(*args, **kwargs):
  mod = cms.EDProducer('EwkElecDQM',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
