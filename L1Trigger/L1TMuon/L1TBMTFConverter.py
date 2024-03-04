import FWCore.ParameterSet.Config as cms

def L1TBMTFConverter(**kwargs):
  mod = cms.EDProducer('L1TBMTFConverter',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
