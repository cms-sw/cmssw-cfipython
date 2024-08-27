import FWCore.ParameterSet.Config as cms

def FFTJetVertexAdder(**kwargs):
  mod = cms.EDProducer('FFTJetVertexAdder',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
