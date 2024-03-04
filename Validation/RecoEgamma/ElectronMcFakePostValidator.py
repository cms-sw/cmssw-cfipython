import FWCore.ParameterSet.Config as cms

def ElectronMcFakePostValidator(**kwargs):
  mod = cms.EDProducer('ElectronMcFakePostValidator',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
