import FWCore.ParameterSet.Config as cms

def EEHltTask(*args, **kwargs):
  mod = cms.EDProducer('EEHltTask',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
