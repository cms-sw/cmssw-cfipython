import FWCore.ParameterSet.Config as cms

def ElectronIdMVAProducer(**kwargs):
  mod = cms.EDFilter('ElectronIdMVAProducer',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
