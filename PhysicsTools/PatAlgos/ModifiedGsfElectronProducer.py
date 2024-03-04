import FWCore.ParameterSet.Config as cms

def ModifiedGsfElectronProducer(**kwargs):
  mod = cms.EDProducer('ModifiedGsfElectronProducer',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
