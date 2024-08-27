import FWCore.ParameterSet.Config as cms

def SimpleGeant4ePropagatorTest(**kwargs):
  mod = cms.EDAnalyzer('SimpleGeant4ePropagatorTest',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
