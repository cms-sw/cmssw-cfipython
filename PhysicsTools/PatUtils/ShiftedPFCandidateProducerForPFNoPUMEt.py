import FWCore.ParameterSet.Config as cms

def ShiftedPFCandidateProducerForPFNoPUMEt(**kwargs):
  mod = cms.EDProducer('ShiftedPFCandidateProducerForPFNoPUMEt',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
