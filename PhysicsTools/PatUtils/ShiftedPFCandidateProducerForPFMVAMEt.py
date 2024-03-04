import FWCore.ParameterSet.Config as cms

def ShiftedPFCandidateProducerForPFMVAMEt(**kwargs):
  mod = cms.EDProducer('ShiftedPFCandidateProducerForPFMVAMEt',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
