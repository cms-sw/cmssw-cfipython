import FWCore.ParameterSet.Config as cms

def ShiftedPATPhotonProducer(**kwargs):
  mod = cms.EDProducer('ShiftedPATPhotonProducer',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
