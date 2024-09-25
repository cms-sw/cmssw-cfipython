import FWCore.ParameterSet.Config as cms

def CandViewPtIsolationProducer(*args, **kwargs):
  mod = cms.EDProducer('CandViewPtIsolationProducer',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
