import FWCore.ParameterSet.Config as cms

def L1GTDigiToRaw(*args, **kwargs):
  mod = cms.EDProducer('L1GTDigiToRaw',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
