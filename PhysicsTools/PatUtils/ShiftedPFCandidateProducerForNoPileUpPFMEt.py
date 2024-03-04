import FWCore.ParameterSet.Config as cms

def ShiftedPFCandidateProducerForNoPileUpPFMEt(**kwargs):
  mod = cms.EDProducer('ShiftedPFCandidateProducerForNoPileUpPFMEt',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
