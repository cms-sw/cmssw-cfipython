import FWCore.ParameterSet.Config as cms

def ElectronConversionRejectionValidator(**kwargs):
  mod = cms.EDProducer('ElectronConversionRejectionValidator',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
