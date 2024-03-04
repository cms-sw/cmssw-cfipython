import FWCore.ParameterSet.Config as cms

def DTROS8FileReader(**kwargs):
  mod = cms.EDProducer('DTROS8FileReader',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
