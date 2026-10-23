import FWCore.ParameterSet.Config as cms

def PFCandidateDQMAnalyzer(*args, **kwargs):
  mod = cms.EDProducer('PFCandidateDQMAnalyzer',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
