import FWCore.ParameterSet.Config as cms

def ProblemTestClient_t1(*args, **kwargs):
  mod = cms.EDAnalyzer('ProblemTestClient_t1',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
