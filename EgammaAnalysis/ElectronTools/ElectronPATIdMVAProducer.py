import FWCore.ParameterSet.Config as cms

def ElectronPATIdMVAProducer(**kwargs):
  mod = cms.EDProducer('ElectronPATIdMVAProducer',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
