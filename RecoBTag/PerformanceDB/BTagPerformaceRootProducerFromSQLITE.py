import FWCore.ParameterSet.Config as cms

def BTagPerformaceRootProducerFromSQLITE(*args, **kwargs):
  mod = cms.EDAnalyzer('BTagPerformaceRootProducerFromSQLITE',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
