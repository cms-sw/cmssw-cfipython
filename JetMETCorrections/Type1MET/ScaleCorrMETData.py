import FWCore.ParameterSet.Config as cms

def ScaleCorrMETData(*args, **kwargs):
  mod = cms.EDProducer('ScaleCorrMETData',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
