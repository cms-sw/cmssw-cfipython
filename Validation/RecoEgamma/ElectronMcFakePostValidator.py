import FWCore.ParameterSet.Config as cms

def ElectronMcFakePostValidator(*args, **kwargs):
  mod = cms.EDProducer('ElectronMcFakePostValidator',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
