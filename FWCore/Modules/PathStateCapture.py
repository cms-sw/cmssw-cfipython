import FWCore.ParameterSet.Config as cms

def PathStateCapture(*args, **kwargs):
  mod = cms.EDProducer('PathStateCapture',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
