import FWCore.ParameterSet.Config as cms

def VersionedGsfElectronIdProducer(**kwargs):
  mod = cms.EDProducer('VersionedGsfElectronIdProducer',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
