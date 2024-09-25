import FWCore.ParameterSet.Config as cms

def QjetsAdder(*args, **kwargs):
  mod = cms.EDProducer('QjetsAdder',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
