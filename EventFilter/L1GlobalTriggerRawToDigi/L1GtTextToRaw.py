import FWCore.ParameterSet.Config as cms

def L1GtTextToRaw(*args, **kwargs):
  mod = cms.EDProducer('L1GtTextToRaw',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
