import FWCore.ParameterSet.Config as cms

def CastorDigiToRaw(*args, **kwargs):
  mod = cms.EDProducer('CastorDigiToRaw',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
