import FWCore.ParameterSet.Config as cms

def JetSignalVertexCompatibility(**kwargs):
  mod = cms.EDProducer('JetSignalVertexCompatibility',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
