import FWCore.ParameterSet.Config as cms

def trgMatchedGsfElectronProducer(**kwargs):
  mod = cms.EDProducer('trgMatchedGsfElectronProducer',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
