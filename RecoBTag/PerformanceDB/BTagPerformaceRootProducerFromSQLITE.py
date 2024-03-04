import FWCore.ParameterSet.Config as cms

def BTagPerformaceRootProducerFromSQLITE(**kwargs):
  mod = cms.EDAnalyzer('BTagPerformaceRootProducerFromSQLITE',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
