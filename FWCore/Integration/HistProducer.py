import FWCore.ParameterSet.Config as cms

def HistProducer(*args, **kwargs):
  mod = cms.EDProducer('HistProducer',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
