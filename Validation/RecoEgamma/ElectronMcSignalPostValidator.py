import FWCore.ParameterSet.Config as cms

def ElectronMcSignalPostValidator(*args, **kwargs):
  mod = cms.EDProducer('ElectronMcSignalPostValidator',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
