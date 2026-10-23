import FWCore.ParameterSet.Config as cms

def RecoMETExtractor(*args, **kwargs):
  mod = cms.EDProducer('RecoMETExtractor',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
