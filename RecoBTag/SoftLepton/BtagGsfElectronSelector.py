import FWCore.ParameterSet.Config as cms

def BtagGsfElectronSelector(**kwargs):
  mod = cms.EDProducer('BtagGsfElectronSelector',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
