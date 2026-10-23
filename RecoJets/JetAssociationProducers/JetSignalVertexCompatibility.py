import FWCore.ParameterSet.Config as cms

def JetSignalVertexCompatibility(*args, **kwargs):
  mod = cms.EDProducer('JetSignalVertexCompatibility',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
