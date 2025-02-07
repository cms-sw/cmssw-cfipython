import FWCore.ParameterSet.Config as cms

def CandPtIsolationProducer(*args, **kwargs):
  mod = cms.EDProducer('CandPtIsolationProducer',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
