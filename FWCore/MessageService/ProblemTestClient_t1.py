import FWCore.ParameterSet.Config as cms

def ProblemTestClient_t1(**kwargs):
  mod = cms.EDAnalyzer('ProblemTestClient_t1',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
