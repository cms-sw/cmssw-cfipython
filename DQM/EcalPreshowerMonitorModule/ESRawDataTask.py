import FWCore.ParameterSet.Config as cms

def ESRawDataTask(*args, **kwargs):
  mod = cms.EDProducer('ESRawDataTask',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
