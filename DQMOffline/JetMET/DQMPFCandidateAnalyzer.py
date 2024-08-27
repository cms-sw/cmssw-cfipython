import FWCore.ParameterSet.Config as cms

def DQMPFCandidateAnalyzer(**kwargs):
  mod = cms.EDProducer('DQMPFCandidateAnalyzer',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
