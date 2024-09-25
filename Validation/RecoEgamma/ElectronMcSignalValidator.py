import FWCore.ParameterSet.Config as cms

def ElectronMcSignalValidator(*args, **kwargs):
  mod = cms.EDProducer('ElectronMcSignalValidator',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
