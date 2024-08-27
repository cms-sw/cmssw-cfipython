import FWCore.ParameterSet.Config as cms

def trgMatchedElectronProducer(**kwargs):
  mod = cms.EDProducer('trgMatchedElectronProducer',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
