import FWCore.ParameterSet.Config as cms

def ShiftedPATMuonProducer(**kwargs):
  mod = cms.EDProducer('ShiftedPATMuonProducer',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
