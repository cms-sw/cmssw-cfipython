import FWCore.ParameterSet.Config as cms

def GsfElectronFromPVSelector(**kwargs):
  mod = cms.EDProducer('GsfElectronFromPVSelector',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
