import FWCore.ParameterSet.Config as cms

def PackedPFCandidateRefMixer(*args, **kwargs):
  mod = cms.EDProducer('PackedPFCandidateRefMixer',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
