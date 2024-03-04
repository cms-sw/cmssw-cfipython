import FWCore.ParameterSet.Config as cms

def PackedPFCandidateRefMixer(**kwargs):
  mod = cms.EDProducer('PackedPFCandidateRefMixer',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
