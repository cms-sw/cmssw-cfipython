import FWCore.ParameterSet.Config as cms

def ShiftedPATTauProducer(**kwargs):
  mod = cms.EDProducer('ShiftedPATTauProducer',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
