import FWCore.ParameterSet.Config as cms

def DigiTask(*args, **kwargs):
  mod = cms.EDProducer('DigiTask',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
