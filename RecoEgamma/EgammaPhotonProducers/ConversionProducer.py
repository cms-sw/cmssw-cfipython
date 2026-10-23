import FWCore.ParameterSet.Config as cms

def ConversionProducer(*args, **kwargs):
  mod = cms.EDProducer('ConversionProducer',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
