import FWCore.ParameterSet.Config as cms

def ShiftedPFCandidateProducerByMatchedObject(*args, **kwargs):
  mod = cms.EDProducer('ShiftedPFCandidateProducerByMatchedObject',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
