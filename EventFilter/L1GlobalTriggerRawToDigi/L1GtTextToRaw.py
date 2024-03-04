import FWCore.ParameterSet.Config as cms

def L1GtTextToRaw(**kwargs):
  mod = cms.EDProducer('L1GtTextToRaw',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
