import FWCore.ParameterSet.Config as cms

def trgMatchElectronProducer(**kwargs):
  mod = cms.EDProducer('trgMatchElectronProducer',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
