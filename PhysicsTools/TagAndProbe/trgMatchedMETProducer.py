import FWCore.ParameterSet.Config as cms

def trgMatchedMETProducer(*args, **kwargs):
  mod = cms.EDProducer('trgMatchedMETProducer',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
