import FWCore.ParameterSet.Config as cms

def DTROS25FileReader(**kwargs):
  mod = cms.EDProducer('DTROS25FileReader',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
