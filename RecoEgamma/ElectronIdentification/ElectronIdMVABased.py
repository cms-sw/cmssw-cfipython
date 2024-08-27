import FWCore.ParameterSet.Config as cms

def ElectronIdMVABased(**kwargs):
  mod = cms.EDProducer('ElectronIdMVABased',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
