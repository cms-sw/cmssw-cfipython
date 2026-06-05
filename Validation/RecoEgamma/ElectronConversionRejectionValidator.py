import FWCore.ParameterSet.Config as cms

def ElectronConversionRejectionValidator(*args, **kwargs):
  mod = cms.EDProducer('ElectronConversionRejectionValidator',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
