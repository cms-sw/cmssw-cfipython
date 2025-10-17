import FWCore.ParameterSet.Config as cms

def VertexCompositeCandidateDaughtersRekeyer(*args, **kwargs):
  mod = cms.EDProducer('VertexCompositeCandidateDaughtersRekeyer',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
