import FWCore.ParameterSet.Config as cms

def ShiftedPFCandidateProducerForNoPileUpPFMEt(*args, **kwargs):
  mod = cms.EDProducer('ShiftedPFCandidateProducerForNoPileUpPFMEt',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
