import FWCore.ParameterSet.Config as cms

def ShiftedPFCandidateProducerForPFMVAMEt(*args, **kwargs):
  mod = cms.EDProducer('ShiftedPFCandidateProducerForPFMVAMEt',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
