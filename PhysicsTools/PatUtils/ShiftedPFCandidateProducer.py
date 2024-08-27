import FWCore.ParameterSet.Config as cms

def ShiftedPFCandidateProducer(**kwargs):
  mod = cms.EDProducer('ShiftedPFCandidateProducer',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
