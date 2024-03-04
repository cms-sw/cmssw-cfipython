import FWCore.ParameterSet.Config as cms

def VersionedPatElectronIdProducer(**kwargs):
  mod = cms.EDProducer('VersionedPatElectronIdProducer',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
