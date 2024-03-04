import FWCore.ParameterSet.Config as cms

def ESRawDataTask(**kwargs):
  mod = cms.EDProducer('ESRawDataTask',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
