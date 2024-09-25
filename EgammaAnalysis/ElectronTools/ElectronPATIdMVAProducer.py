import FWCore.ParameterSet.Config as cms

def ElectronPATIdMVAProducer(*args, **kwargs):
  mod = cms.EDProducer('ElectronPATIdMVAProducer',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
