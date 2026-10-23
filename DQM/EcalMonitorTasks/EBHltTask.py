import FWCore.ParameterSet.Config as cms

def EBHltTask(*args, **kwargs):
  mod = cms.EDProducer('EBHltTask',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
