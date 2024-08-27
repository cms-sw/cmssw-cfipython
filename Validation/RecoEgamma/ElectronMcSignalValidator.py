import FWCore.ParameterSet.Config as cms

def ElectronMcSignalValidator(**kwargs):
  mod = cms.EDProducer('ElectronMcSignalValidator',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
