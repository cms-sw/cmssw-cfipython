import FWCore.ParameterSet.Config as cms

def RecoChargedCandidateMatchedProbeMaker(**kwargs):
  mod = cms.EDProducer('RecoChargedCandidateMatchedProbeMaker',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
