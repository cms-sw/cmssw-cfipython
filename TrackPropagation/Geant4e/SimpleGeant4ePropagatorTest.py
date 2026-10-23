import FWCore.ParameterSet.Config as cms

def SimpleGeant4ePropagatorTest(*args, **kwargs):
  mod = cms.EDAnalyzer('SimpleGeant4ePropagatorTest',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
