import FWCore.ParameterSet.Config as cms

def DTuROSDigiToRaw(*args, **kwargs):
  mod = cms.EDProducer('DTuROSDigiToRaw',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
