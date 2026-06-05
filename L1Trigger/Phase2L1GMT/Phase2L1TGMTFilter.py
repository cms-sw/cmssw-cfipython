import FWCore.ParameterSet.Config as cms

def Phase2L1TGMTFilter(*args, **kwargs):
  mod = cms.EDProducer('Phase2L1TGMTFilter',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
