import FWCore.ParameterSet.Config as cms

def StGenEventReco(*args, **kwargs):
  mod = cms.EDProducer('StGenEventReco',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
