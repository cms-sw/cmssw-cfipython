import FWCore.ParameterSet.Config as cms

def L1TkHTMissEmulatorProducer(*args, **kwargs):
  mod = cms.EDProducer('L1TkHTMissEmulatorProducer',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
