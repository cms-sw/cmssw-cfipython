import FWCore.ParameterSet.Config as cms

def CandPtIsolationProducerNew(*args, **kwargs):
  mod = cms.EDProducer('CandPtIsolationProducerNew',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
