import FWCore.ParameterSet.Config as cms

def MinPatMETProducer(*args, **kwargs):
  mod = cms.EDProducer('MinPatMETProducer',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
