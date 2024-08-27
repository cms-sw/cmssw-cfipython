import FWCore.ParameterSet.Config as cms

def ModifiedElectronProducer(**kwargs):
  mod = cms.EDProducer('ModifiedElectronProducer',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
