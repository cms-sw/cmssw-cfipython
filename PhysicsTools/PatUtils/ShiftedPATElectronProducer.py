import FWCore.ParameterSet.Config as cms

def ShiftedPATElectronProducer(**kwargs):
  mod = cms.EDProducer('ShiftedPATElectronProducer',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
